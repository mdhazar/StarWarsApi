from flask import Blueprint

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Star Wars Characters API</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                padding: 30px;
                background: white;
                border-radius: 15px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 10px;
                font-size: 2.5em;
            }
            .subtitle {
                text-align: center;
                color: #7f8c8d;
                margin-bottom: 30px;
                font-style: italic;
            }
            .api-links {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin: 30px 0;
            }
            .api-link {
                display: block;
                padding: 15px;
                background: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                text-align: center;
                transition: all 0.3s ease;
            }
            .api-link:hover {
                background: #2980b9;
                transform: translateY(-2px);
            }
            .swagger-link {
                background: #27ae60;
                font-size: 1.2em;
                font-weight: bold;
            }
            .swagger-link:hover {
                background: #229954;
            }
            .tech-stack {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 10px;
                margin: 30px 0;
            }
            .tech-badge {
                padding: 5px 12px;
                background: #e74c3c;
                color: white;
                border-radius: 20px;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 Star Wars Characters API</h1>
            <p class="subtitle">A comprehensive REST API for managing Star Wars characters</p>
        
            
            <div class="api-links">
                <a href="/docs/" class="api-link swagger-link">📖 Interactive API Documentation (Swagger)</a>
                <a href="/api/characters" class="api-link">👑 All Characters</a>
                <a href="/api/characters/names" class="api-link">📝 Character Names</a>
                <a href="/api/characters/affiliations" class="api-link">⚔️ Affiliations</a>
                <a href="/api/characters/species" class="api-link">🧬 Species</a>
                <a href="/api/characters/homeworld" class="api-link">🌍 Homeworlds</a>
            </div>
            
            <div class="tech-stack">
                <span class="tech-badge">Flask</span>
                <span class="tech-badge">Flask-RESTX</span>
                <span class="tech-badge">MongoDB</span>
                <span class="tech-badge">Marshmallow</span>
                <span class="tech-badge">Swagger/OpenAPI</span>
                <span class="tech-badge">CORS</span>
            </div>
            
            <div style="text-align: center; margin-top: 40px; color: #7f8c8d;">
                <p>🔗 <strong>API Base URL:</strong> <code>http://localhost:8000/api</code></p>
                <p>Built with modern Python web development best practices</p>
            </div>
        </div>
    </body>
    </html>
    """
