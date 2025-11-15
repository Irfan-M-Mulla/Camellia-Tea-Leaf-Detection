## 🍵 Tea Leaf Disease Classifier - README

---

### 🌟 Project Overview

This is a web application built with **Flask** that uses a deep learning model to classify the disease present in an image of a tea leaf. The model is based on the **VGG16** architecture and can identify **8 different classes** including various diseases and a healthy state.

### 🍃 Classes Identified

The classification model can identify the following conditions:

- Anthracnose
- Algal Leaf
- Bird Eye Spot
- Brown Blight
- Gray Light
- **Healthy**
- Red Leaf Spot
- White Spot

Upon prediction, the application also provides specific **fertilizer recommendations** and **prevention tips** for the identified disease.

---

### ⚙️ Prerequisites

To run this application, you need to have **Python 3.x** and the following libraries installed:

- `Flask`
- `tensorflow` (or `tensorflow-cpu`)
- `numpy`
- `keras` (usually included with `tensorflow`)
- `scikit-learn` (not explicitly used in `app.py` but often helpful)

You can install the dependencies using pip:

```bash
pip install flask tensorflow numpy
```

---

### 📂 File Structure

The project has the following key directories and files:

| File/Folder                         | Description                                                                                                   |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| `app.py`                            | The main Flask application file. Handles routes, image upload, preprocessing, prediction, and result display. |
| `templates/`                        | Contains the HTML files (`index.html`, `About.html`, `Tryit.html`) for the web interface.                     |
| `static/`                           | Stores static assets like CSS, images, and the `uploads` folder.                                              |
| `static/uploads/`                   | Stores the images uploaded by the user for prediction.                                                        |
| `VGG16-Tea-Leaves-disease-model.h5` | The default, trained Keras/HDF5 model file.                                                                   |
| `**Other_models/**`                 | **[CRITICAL]** This folder is intended to hold alternative or future machine learning models.                 |

## LINK FOR THE MODELS="https://drive.google.com/file/d/15lVlZz6PmPyNlW9ipr1r_ufpZKY38xDa/view?usp=drive_link"

### 🚀 Getting Started

#### 1\. Model Setup

**Crucially, the trained ML model must be explicitly selected and placed or linked in the root directory for `app.py` to load it.**

The current application loads the model with the filename `"VGG16-Tea-Leaves-disease-model.h5"`.

**To switch to a model from `Other_models/`:**

1.  **Open** `app.py`.
2.  **Change** the model loading line:

    ```python
    # Original:
    modeln = load_model("VGG16-Tea-Leaves-disease-model.h5")

    # Example for a model named 'EfficientNet-Tea.h5' in Other_models:
    # modeln = load_model("Other_models/EfficientNet-Tea.h5")
    ```

    _Note: Ensure the file path is correct relative to `app.py`._

#### 2\. Running the Application

1.  Ensure you are in the root directory of the project.

2.  Run the Flask application:

    ```bash
    python app.py
    ```

3.  The application will start, typically on port **8989** (as configured in `app.py`). Open your web browser and navigate to:

    ```
    http://127.0.0.1:8989/
    ```

---

### 🛠️ Model Inspection

The provided `inspect_model.py` and `load_model.py` scripts can be used to load the model and display its architecture summary.

To inspect the currently used model:

```bash
python inspect_model.py
# OR
python load_model.py
```

_Note: If you have changed the model path in `app.py` as described above, you may need to update the model path in the inspection scripts as well._

---

### 🛑 Stopping the Application

Press **Ctrl + C** in the terminal where the Flask application is running to stop the server.

---
