# HealthAI

HealthAI is an intelligent platform designed to assist with patient registration and health analysis. It includes functionalities such as user registration, health check-ups, and predictive diagnostics using advanced algorithms.

## Features

- **User Registration:**
  - Register patients with details like name, age, contact, and medical history.
  - Password confirmation for secure access.

- **Health Check-Up Form:**
  - Collects vital data like blood pressure, cholesterol levels, and other health indicators.
  - Supports various input types such as radio buttons, integers, and floating-point numbers.

- **Custom Filters:**
  - Dynamically add CSS classes and placeholders to form fields using Django template filters.

## Technologies Used

- **Backend:** Django Framework
- **Frontend:** TailwindCSS for styling
- **Database:** SQLite (default Django database, customizable to other databases like PostgreSQL or MySQL)
- **Version Control:** Git

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/healthAI.git
   cd healthAI
   ```

2. Set up a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply Migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the Development Server:
   ```bash
   python manage.py runserver
   ```

## Usage

### User Registration
Navigate to the `/register/` endpoint to register a new patient. Ensure all required fields are filled, and passwords match.

### Health Check-Up
Visit the `/checkup/` endpoint to input health data. The form captures vital signs and provides health insights.

### TailwindCSS Styling
- Modify the `base.html` or specific templates to apply custom styles using TailwindCSS.

```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or support, please reach out to:

- **Email:** bigirwarft76@gmail.com
- **GitHub:** [yinvestor](https://github.com/yinvestor)

---
Thank you for using HealthAI! Together, we can make healthcare more accessible and efficient.

