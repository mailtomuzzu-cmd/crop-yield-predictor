
import gradio as gr
import joblib
import pandas as pd

model = joblib.load('crop_yield_model.pkl')

def predict_yield(area, item, year, rainfall, pesticides, temperature):
    input_data = pd.DataFrame([[area, item, year, rainfall, pesticides, temperature]],
                              columns=['Area','Item','Year',
                                      'average_rain_fall_mm_per_year',
                                      'pesticides_tonnes','avg_temp'])
    prediction = model.predict(input_data)
    return f"Predicted Yield: {round(prediction[0], 2)} hg/ha"

app = gr.Interface(
    fn=predict_yield,
    inputs=[
        gr.Number(label="Area Code (0-100)", value=0),
        gr.Number(label="Crop Code (0-80)", value=6),
        gr.Number(label="Year", value=2000),
        gr.Number(label="Rainfall mm/year", value=1485.0),
        gr.Number(label="Pesticides tonnes", value=121.0),
        gr.Number(label="Temperature °C", value=16.37)
    ],
    outputs=gr.Text(label="Prediction"),
    title="Crop Yield Predictor",
    description="Enter farming conditions to predict crop yield in hg/ha"
)

app.launch()
