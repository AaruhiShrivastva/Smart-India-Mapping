# Smart India Mapping

A full-stack geospatial analysis platform for mapping and analyzing satellite imagery across Indian states using AI/ML capabilities.

## Overview

Smart India Mapping combines satellite image analysis with interactive mapping to provide insights into geographical data across India. The platform features real-time data visualization, geospatial analytics, and AI-powered satellite imagery analysis.

## Tech Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.x
- **Key Libraries**:
  - `geopandas` - Geospatial data analysis
  - `scikit-learn` - Machine learning
  - `opencv-python` - Image processing
  - `pandas` - Data manipulation
  - `python-jose` - Authentication
  - `passlib` - Password hashing

### Frontend
- **Framework**: Next.js 16.2.6
- **Language**: TypeScript
- **UI Components**:
  - `react-leaflet` - Interactive maps
  - `recharts` - Data visualization
  - `lucide-react` - Icons
  - `tailwindcss` - Styling
  - `framer-motion` - Animations

## Project Structure

```
smart-india-mapping/
├── ai_models/              # ML models and satellite image analysis
│   ├── generate_mock_satellite.py
│   ├── satellite_analysis.py
│   └── test_analysis.py
├── backend/                # FastAPI server
│   ├── main.py            # Application entry point
│   ├── auth.py            # Authentication logic
│   ├── database.py        # Database configuration
│   ├── models.py          # Data models
│   ├── requirements.txt   # Python dependencies
│   └── api/               # API endpoints
│       ├── auth.py        # Auth endpoints
│       └── geospatial.py  # Geospatial endpoints
├── frontend/              # Next.js application
│   ├── src/
│   │   ├── app/           # Next.js app directory
│   │   │   ├── page.tsx          # Home page
│   │   │   ├── dashboard/        # Dashboard page
│   │   │   ├── login/            # Login page
│   │   │   └── register/         # Registration page
│   │   └── components/    # Reusable components
│   │       ├── MapComponent.tsx
│   │       ├── AnalyticsDashboard.tsx
│   │       ├── Sidebar.tsx
│   │       └── StatCard.tsx
│   └── package.json       # Node dependencies
├── data/                  # Static data and assets
│   ├── india_states.json # State boundary data
│   └── images/           # Satellite imagery and assets
└── docs/                 # Documentation
```

## Prerequisites

- **Python 3.9+**
- **Node.js 18+**
- **npm** or **yarn**

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd smart-india-mapping
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
# or
yarn install
```

## Running the Application

### Start Backend Server

```bash
cd backend
# Ensure virtual environment is activated
python main.py
```

The backend API will be available at `http://localhost:8000`

### Start Frontend Development Server

```bash
cd frontend
npm run dev
# or
yarn dev
```

The frontend will be available at `http://localhost:3000`

## Features

- **Interactive Map Visualization**: Browse Indian states with Leaflet-based mapping
- **Satellite Image Analysis**: AI-powered analysis of satellite imagery using scikit-learn and OpenCV
- **Analytics Dashboard**: Real-time metrics and data visualization with Recharts
- **User Authentication**: Secure login and registration system
- **Geospatial API**: RESTful API for geospatial queries and data
- **Responsive Design**: Mobile-friendly interface with Tailwind CSS

## Development

### Running Tests

```bash
cd ai_models
python test_analysis.py
```

### Available Scripts

#### Frontend
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

#### Backend
- `python main.py` - Start development server
- `uvicorn main:app --reload` - Start with auto-reload

## API Documentation

Once the backend is running, access the interactive API documentation at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Configuration

Create a `.env` file in the `backend` directory for environment variables:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```

## Contributing

1. Create a feature branch (`git checkout -b feature/amazing-feature`)
2. Commit your changes (`git commit -m 'Add amazing feature'`)
3. Push to the branch (`git push -u origin feature/amazing-feature`)
4. Open a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues, questions, or suggestions, please create an issue in the repository.

---

**Last Updated**: May 2026
