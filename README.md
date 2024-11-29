

# **Crop Prediction Application**

An interactive web application for predicting crop yields based on input parameters using machine learning. Built with **Streamlit**, this application leverages pre-trained models and provides a user-friendly interface for real-time predictions.

---

## **Live Application**
Try the app online: [Crop Prediction Application](https://cropprediction-eku9panrggy6frvnk7voh4.streamlit.app/)

---

## **Features**
- **Machine Learning Model**: Pre-trained model to predict crop yields based on dataset parameters.
- **Interactive UI**: Built using **Streamlit**, providing a seamless user experience.
- **Ready for Deployment**: Easily scalable and deployable to cloud platforms like Streamlit Cloud.
- **Configurable & Extendable**: Flexible project structure for customization.

---

## **Project Structure**
Here’s an overview of the repository structure:

```
crop_prediction/
├── .vscode/                   # VS Code configuration files
├── data/                      # Directory containing the dataset
│   └── agriculture_dataset.csv
├── src/                       # Source code modules
│   ├── main.py                # Main processing script
│   ├── init.py                # Initialization script
├── .gitignore                 # Files to ignore in Git
├── LICENSE                    # License for the project
├── README.md                  # Documentation file
├── app.py                     # Streamlit application
├── label_encoders.pkl         # Serialized label encoder for preprocessing
├── requirements.txt           # Required Python dependencies
├── scaler.pkl                 # Serialized scaler for normalization
├── yield_prediction_model.pkl # Pre-trained crop prediction model
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/crop_prediction.git
cd crop_prediction
```

### **2. Install Dependencies**
Ensure you have Python installed. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### **3. Run the Application**
Start the Streamlit application locally:
```bash
streamlit run app.py
```

---

## **Dataset Requirements**
- The application requires the dataset `agriculture_dataset.csv` to be present in the `data` directory.
- Ensure the file paths in your scripts are **relative** to avoid deployment issues. Example:
    ```python
    import os
    file_path = os.path.join(os.path.dirname(__file__), "../data/agriculture_dataset.csv")
    ```

---

## **Deployment**
This project is already deployed on **Streamlit Cloud**. To deploy your own version:
1. Push the project to your GitHub repository.
2. Link the repository with **Streamlit Cloud**.
3. Ensure all dependencies are listed in `requirements.txt`.
4. Verify dataset and model files are included in the deployment package.

---

## **Troubleshooting**
### Common Issues:
1. **FileNotFoundError**:  
   - Ensure the dataset and model files are present in the expected locations.
   - Use relative paths in code.
2. **Permission Denied on Git Push**:
   - Verify your GitHub credentials.
   - Update the repository URL using HTTPS or SSH.

### Debugging Tools:
- Print the working directory and file paths in the app to debug:
    ```python
    import os
    print("Current Working Directory:", os.getcwd())
    ```

---

## **Contributing**
We welcome contributions! Fork the repository, make changes, and submit a pull request. Suggestions for improvements are always appreciated.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

## **Author**
Developed by [Your Name](https://github.com/<your-username>). If you have any questions or feedback, feel free to reach out!

---

This structure ensures all critical aspects are covered, making the README informative and easy to navigate. Let me know if you need any edits or further customization!
