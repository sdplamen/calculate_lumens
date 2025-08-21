# Lumen Calculator

This project is a web application and REST API for calculating the recommended lumen levels for various types of spaces. It helps users determine the appropriate amount of light needed for a room or area based on its intended use and size.

The application provides minimum, maximum, and average lumen recommendations based on industry-standard lux levels for a wide range of space types, from residential rooms to commercial and industrial environments.

## Features

*   **Web Interface:** A user-friendly web form to calculate lumens for a specific space type and area.
*   **REST API:** A set of API endpoints to programmatically access the lumen calculation functionality.
*   **Comprehensive Space Types:** Includes a wide variety of predefined space types with their corresponding lux ranges.
*   **Command-Line Interface (CLI):** A script to run the calculator from the command line.
*   **Django Backend:** Built with the robust and scalable Django web framework.

## Technologies Used

*   **Backend:** Django, Django REST Framework, Celery
*   **Frontend:** HTML, CSS, JavaScript
*   **Database:** PostgreSQL (as indicated by `psycopg2` dependency)
*   **File Storage:** Cloudinary

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.12
*   pip (Python package installer)
*   PostgreSQL (or another database of your choice)

## Usage

### Web Interface

1.  Navigate to the home page of the application in your web browser.
2.  Select a "Space Type" from the dropdown menu.
3.  Enter the "Area" of the space in square meters.
4.  Click the "Calculate" button to see the recommended lumen levels.

### REST API

The API provides endpoints for interacting with the lumen calculator.

#### Endpoints

*   `POST /api/calculate/`
    *   Calculates the lumen levels for a given space type and area.
    *   **Request Body:**
        ```json
        {
            "space_type": "kitchen",
            "area": 20
        }
        ```
    *   **Success Response (200 OK):**
        ```json
        {
            "space_type": "kitchen",
            "area": 20,
            "min_lux": 300,
            "max_lux": 750,
            "min_lumens": 6000,
            "max_lumens": 15000,
            "avg_lumens": 10500
        }
        ```
    *   **Error Response (400 Bad Request):**
        ```json
        {
            "error": "Space type 'invalid_space' not found or invalid."
        }
        ```

*   `GET /api/calculate/`
    *   Retrieves a list of available space types.
    *   **Success Response (200 OK):**
        ```json
        {
            "space_types": [
                "general living",
                "kitchen",
                "kitchen task",
                ...
            ]
        }
        ```

### Command-Line Interface (CLI)

You can also use the `calc_lumens.py` script to perform calculations from the command line.

```bash
python calc_lumens.py
```

The script will prompt you to enter the space type and area.
