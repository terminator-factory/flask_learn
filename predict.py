from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

# загружаем модель
model_file_path = "model/project_1_mastercard.sav"
model = pickle.load(open(model_file_path, 'rb'))

app = Flask('mastercard')

# предсказываем закрывающую цену
@app.route('/', methods=['POST'])
def predict_close():
    try:
        customer = request.get_json()
        input_dataframe = pd.DataFrame(customer, index=[0])
        input_data = np.log1p(input_dataframe)
        prediction = model.predict(input_data)
        prediction_expm = round(*np.expm1(prediction), 2)
        result = {'Closing Price' : prediction_expm}
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9697)