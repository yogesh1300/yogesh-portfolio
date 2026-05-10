# Complete Plan: Embed Live Previews in Portfolio Website

This is a detailed A-to-Z guide to embed live project outputs directly in your portfolio with screenshots and interactive demos.

---

## PHASE 1: PREPARE YOUR PROJECTS

### Step 1.1: List Your Projects
Collect all your projects and categorize them by type:

```
PROJECT INVENTORY:

Web Projects (HTML/CSS/JavaScript):
- [ ] Luxury Motorbike Purchase Portal
- [ ] To-Do List App
- [ ] E-Commerce Website
- [ ] Travel Website

Python/Data Projects:
- [ ] Titanic Survival Prediction
- [ ] AI Information Chatbot (Rasa)

IoT/Embedded Projects:
- [ ] Virtual Eye Obstacle System
- [ ] Smart Irrigation System
```

**ACTION:** Go to your laptop, find all project folders and list them above.

---

### Step 1.2: Organize Project Folders
Create a structured folder layout:

```
Projects_Master/
├── 1-luxury-motorbike-portal/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   ├── README.md
│   └── screenshot.png
├── 2-ai-chatbot-rasa/
│   ├── main.py
│   ├── requirements.txt
│   ├── README.md
│   └── screenshot.png
├── 3-titanic-prediction/
│   ├── notebook.ipynb
│   ├── requirements.txt
│   ├── README.md
│   └── screenshot.png
```

**ACTION:** 
1. Create a folder called `c:\Users\acer\OneDrive\Desktop\portfolio\projects`
2. Copy each project into its own subfolder
3. Name folders: `1-project-name`, `2-project-name` (number them for order)

---

## PHASE 2: PREPARE SCREENSHOTS FOR EACH PROJECT

### Step 2.1: Screenshot Every Project Output
For each project, capture a professional screenshot:

**For Web Projects:**
1. Open the project in browser
2. Press `Windows + Shift + S` (Windows Snip tool)
3. Crop the best view
4. Save as `screenshot.png` in the project folder

**For Data/ML Projects:**
1. Open Jupyter notebook or Python output
2. Take screenshot of the visualization/output
3. Save as `screenshot.png`

**For IoT/Embedded:**
1. Take a photo of the working hardware OR screenshot of code diagram
2. Save as `screenshot.png`

**ACTION:** Take screenshots for all 6-8 projects and save them in each project folder.

---

### Step 2.2: Optimize Screenshots
Standardize all screenshots to same dimensions:

- **Recommended size:** 800x450 pixels (16:9 ratio)
- Use an online tool like [tinypng.com](https://tinypng.com) to compress
- Name consistently: `screenshot.png`

---

## PHASE 3: HOST LIVE DEMOS

### Step 3.1: Host Web Projects (HTML/CSS/JavaScript)

**Option A: GitHub Pages (Recommended)**

For each web project:

1. **Create GitHub Repository:**
   - Go to github.com/yogesh1300
   - Click "New Repository"
   - Name: `luxury-motorbike-portal` (or project name)
   - Mark as Public
   - Click "Create Repository"

2. **Upload Project Files:**
   ```bash
   cd path/to/project
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yogesh1300/luxury-motorbike-portal.git
   git push -u origin main
   ```

3. **Enable GitHub Pages:**
   - Go to repository Settings
   - Scroll to "GitHub Pages"
   - Select "main" branch as source
   - Save
   - Wait 2-5 minutes
   - Your live link: `https://yogesh1300.github.io/luxury-motorbike-portal`

**ACTION:** Create GitHub repos for each web project and enable GitHub Pages.

---

### Step 3.2: Host Python Web Apps (Flask/Django)

**Option: Render (Free)**

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Select your GitHub repo
5. Configure:
   - **Name:** project-name
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app` (or your main command)
6. Click "Create Web Service"
7. Live link: `https://project-name-xxxxx.onrender.com`

**ACTION:** Deploy any Flask/Django projects to Render.

---

### Step 3.3: Host AI Chatbots (Rasa)

**Option: Hugging Face Spaces (Free with GPU)**

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create New Space"
3. **Space Name:** `yogesh-ai-chatbot`
4. **License:** OpenRAIL
5. **Space SDK:** Docker
6. Click "Create Space"
7. Upload your Rasa project files
8. Live link: `https://huggingface.co/spaces/yogesh1300/yogesh-ai-chatbot`

**ACTION:** Deploy your Rasa chatbot to Hugging Face Spaces.

---

### Step 3.4: Host Data/ML Projects (Jupyter/Python)

**Option: Streamlit Cloud (Free)**

1. Go to [streamlit.io](https://streamlit.io)
2. Click "Sign in" → Use GitHub
3. Create a simple Python file (`app.py`):
   ```python
   import streamlit as st
   import pandas as pd
   
   st.title("Titanic Survival Prediction")
   # Add your prediction code here
   ```
4. Push to GitHub
5. Deploy from Streamlit Cloud
6. Live link: `https://yogesh-titanic-prediction.streamlit.app`

**ACTION:** Create Streamlit apps for ML/Data projects and deploy.

---

## PHASE 4: CREATE PROJECT DATA FILE

### Step 4.1: Create a JSON File with All Projects

Create file: `c:\Users\acer\OneDrive\Desktop\portfolio\projects-data.json`

```json
{
  "projects": [
    {
      "id": 1,
      "title": "Luxury Motorbike Purchase Portal",
      "description": "Full-stack web application showcasing luxury bikes with booking system and database integration.",
      "category": "Web Development",
      "technologies": ["HTML", "CSS", "JavaScript", "SQL"],
      "screenshot": "projects/1-luxury-motorbike-portal/screenshot.png",
      "github": "https://github.com/yogesh1300/luxury-motorbike-portal",
      "liveDemo": "https://yogesh1300.github.io/luxury-motorbike-portal",
      "description_long": "Built a responsive e-commerce portal for luxury motorbike shopping. Features include product catalog, search functionality, shopping cart, and backend database for booking requests. Implemented working functionality with database integration to store requests and manage product information efficiently."
    },
    {
      "id": 2,
      "title": "AI Information Chatbot",
      "description": "Rasa-based NLP chatbot with intent recognition and automated responses using web data sources.",
      "category": "AI & Machine Learning",
      "technologies": ["Python", "Rasa AI", "ChatGPT", "NLP"],
      "screenshot": "projects/2-ai-chatbot-rasa/screenshot.png",
      "github": "https://github.com/yogesh1300/ai-information-chatbot",
      "liveDemo": "https://huggingface.co/spaces/yogesh1300/yogesh-ai-chatbot",
      "description_long": "Developed an AI chatbot using Rasa framework with integrated Wikipedia data sources. Implemented basic NLP for intent recognition, keyword-driven response retrieval, and natural language understanding. Deployed on Hugging Face Spaces for live interaction."
    },
    {
      "id": 3,
      "title": "Virtual Eye - IoT Obstacle Detection",
      "description": "IoT assistive device built with Arduino and ultrasonic sensors for visually impaired navigation.",
      "category": "IoT & Embedded Systems",
      "technologies": ["Arduino", "C++", "IoT", "Ultrasonic Sensors"],
      "screenshot": "projects/3-virtual-eye-iot/screenshot.png",
      "github": "https://github.com/yogesh1300/virtual-eye-obstacle-detection",
      "liveDemo": "https://github.com/yogesh1300/virtual-eye-obstacle-detection#demo",
      "description_long": "Designed an assistive IoT device using Arduino Uno and HC-SR04 ultrasonic sensors to detect obstacles. When obstacles are detected within 30cm, the system triggers an audio alert. Includes power management, sensor calibration, and real-world testing for accessibility."
    },
    {
      "id": 4,
      "title": "Titanic Survival Prediction",
      "description": "Machine learning model predicting passenger survival using Python, Pandas, and Scikit-learn.",
      "category": "Data Science & ML",
      "technologies": ["Python", "Pandas", "Scikit-learn", "Jupyter"],
      "screenshot": "projects/4-titanic-prediction/screenshot.png",
      "github": "https://github.com/yogesh1300/titanic-survival-prediction",
      "liveDemo": "https://yogesh-titanic-prediction.streamlit.app",
      "description_long": "Built a machine learning model analyzing Titanic dataset to predict passenger survival. Performed data preprocessing, feature engineering, and model evaluation. Achieved 80%+ accuracy using logistic regression and random forest algorithms. Deployed interactive dashboard on Streamlit."
    },
    {
      "id": 5,
      "title": "E-Commerce Website UI",
      "description": "Visually polished e-commerce storefront with product cards, cart interactions, and responsive design.",
      "category": "Web Development",
      "technologies": ["HTML", "CSS", "JavaScript"],
      "screenshot": "projects/5-ecommerce-ui/screenshot.png",
      "github": "https://github.com/yogesh1300/ecommerce-website",
      "liveDemo": "https://yogesh1300.github.io/ecommerce-website",
      "description_long": "Created a fully functional e-commerce website with product grid layout, shopping cart functionality, and checkout flow. Features include product filtering, cart management, and responsive design for desktop and mobile devices."
    },
    {
      "id": 6,
      "title": "To-Do List Application",
      "description": "Simple yet productive task management app with clean UI and local storage functionality.",
      "category": "Web Development",
      "technologies": ["HTML", "CSS", "JavaScript"],
      "screenshot": "projects/6-todo-list/screenshot.png",
      "github": "https://github.com/yogesh1300/todo-list-app",
      "liveDemo": "https://yogesh1300.github.io/todo-list-app",
      "description_long": "Built a ToDo application with local storage to persist tasks. Features include add task, mark complete, delete task, and data persistence using browser localStorage. Minimalist UI focusing on usability."
    }
  ]
}
```

**ACTION:** Update with YOUR actual GitHub repos and live demo links.

---

## PHASE 5: UPDATE PORTFOLIO HTML

### Step 5.1: Update Project Cards with Actual Links

Open `index.html` and replace project card sections with:

```html
<section class="project-grid section" id="projects">
  <article class="project-card">
    <div class="project-media" style="background-image: url('projects/1-luxury-motorbike-portal/screenshot.png')"></div>
    <div class="project-body">
      <h3>Luxury Motorbike Purchase Portal</h3>
      <p>Full-stack web application showcasing luxury bikes with booking system and database integration.</p>
      <div class="tech-badges"><span>HTML</span><span>CSS</span><span>JavaScript</span><span>SQL</span></div>
      <div class="card-actions">
        <a href="https://yogesh1300.github.io/luxury-motorbike-portal" class="small-btn" target="_blank">Live Demo</a>
        <a href="https://github.com/yogesh1300/luxury-motorbike-portal" class="small-btn transparent" target="_blank">GitHub</a>
      </div>
    </div>
  </article>
  <!-- Repeat for other projects -->
</section>
```

**ACTION:** Replace `#` placeholders with real GitHub and live demo URLs.

---

### Step 5.2: Add Project Detail Pages (Optional)

Create individual pages for each project with embedded demos:

File: `c:\Users\acer\OneDrive\Desktop\portfolio\project-details.html`

```html
<section class="project-detail">
  <h1>Luxury Motorbike Purchase Portal</h1>
  <p>Full-stack web application for luxury bike shopping</p>
  
  <div class="embed-container">
    <iframe src="https://yogesh1300.github.io/luxury-motorbike-portal" 
            width="100%" 
            height="600px" 
            frameborder="0">
    </iframe>
  </div>
  
  <div class="project-info">
    <h3>Technologies Used</h3>
    <p>HTML, CSS, JavaScript, SQL</p>
    
    <h3>Features</h3>
    <ul>
      <li>Product catalog with luxury bikes</li>
      <li>Search and filter functionality</li>
      <li>Shopping cart system</li>
      <li>Booking request storage</li>
    </ul>
    
    <a href="https://github.com/yogesh1300/luxury-motorbike-portal">View Code</a>
  </div>
</section>
```

---

## PHASE 6: ADD IFRAME EMBEDDING

### Step 6.1: Update CSS for Embedded Projects

Add to `styles.css`:

```css
.embed-container {
  position: relative;
  width: 100%;
  margin: 30px 0;
  border-radius: 28px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.14);
}

.embed-container iframe {
  border-radius: 24px;
  background: #fff;
}

.project-detail {
  max-width: 1000px;
  margin: 60px auto;
  padding: 40px;
  background: rgba(255, 255, 255, 0.02);
  border-radius: 28px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}
```

---

## PHASE 7: CREATE README FOR EACH PROJECT

### Step 7.1: Create GitHub README

Create `README.md` in each GitHub repo:

```markdown
# Luxury Motorbike Purchase Portal

🚗 A stunning full-stack web application for browsing and booking luxury motorbikes.

## Features
- 🎨 Beautiful, responsive UI
- 🔍 Advanced search and filtering
- 🛒 Shopping cart functionality
- 💾 Database integration for bookings

## Technologies
- HTML5, CSS3, JavaScript
- SQL Database
- Responsive Design

## Live Demo
🔗 [View Live Demo](https://yogesh1300.github.io/luxury-motorbike-portal)

## Screenshots
![Project Screenshot](screenshot.png)

## How to Run Locally
1. Clone this repository
2. Open `index.html` in your browser
3. Start exploring!

## Author
Yogesh M | [GitHub](https://github.com/yogesh1300) | [LinkedIn](https://linkedin.com/in/yogesh-m-bbbaba275)
```

---

## PHASE 8: TEST EVERYTHING

### Step 8.1: Checklist Before Launch

- [ ] All projects uploaded to GitHub
- [ ] All web projects deployed to hosting (GitHub Pages, Netlify, etc.)
- [ ] All screenshots taken and optimized (800x450px)
- [ ] Portfolio HTML updated with real links
- [ ] GitHub links working ✓
- [ ] Live demo links accessible ✓
- [ ] Screenshot images loading ✓
- [ ] Portfolio tested on mobile ✓
- [ ] All buttons clickable ✓

### Step 8.2: Test URLs

For each project, open in browser and verify:

```
☐ GitHub link opens → https://github.com/yogesh1300/project-name
☐ Live demo loads → https://yogesh1300.github.io/project-name
☐ Screenshot visible in portfolio ✓
```

---

## PHASE 9: DEPLOY PORTFOLIO

### Step 9.1: Deploy Portfolio to GitHub Pages

1. Create GitHub repo: `yogesh1300.github.io`
2. Push portfolio files:
   ```bash
   cd c:\Users\acer\OneDrive\Desktop\portfolio
   git init
   git add .
   git commit -m "Initial portfolio commit"
   git branch -M main
   git remote add origin https://github.com/yogesh1300/yogesh1300.github.io.git
   git push -u origin main
   ```
3. Access portfolio: `https://yogesh1300.github.io`

### Step 9.2: Deploy to Netlify (Optional Alternative)

1. Go to [netlify.com](https://netlify.com)
2. Click "Add new site" → "Deploy manually"
3. Drag & drop your portfolio folder
4. Done! You get a live link: `https://xxx.netlify.app`

---

## PHASE 10: SHOWCASE & SHARE

### Step 10.1: Final Portfolio Structure

```
Your Portfolio Link: https://yogesh1300.github.io

Contains:
├── Home Section (Hero with profile)
├── About Me (Skills, interests, background)
├── Projects Section (6 cards with live demos)
├── Skills Section (categorized technologies)
├── Education Section (academic info)
├── Experience Section (internships & certs)
├── Contact Section (email, phone, location)

Each Project Card Shows:
├── Project image/screenshot
├── Project title & description
├── Technology tags
├── "Live Demo" button → Opens working project
├── "GitHub" button → Opens source code
```

### Step 10.2: Share with Seniors/Recruiters

Send them:
```
Portfolio Link: https://yogesh1300.github.io
GitHub Profile: https://github.com/yogesh1300
LinkedIn: https://linkedin.com/in/yogesh-m-bbbaba275

"Click on any project card to see the live demo or explore the code!"
```

---

## QUICK REFERENCE: PROJECT HOSTING CHART

| Project Type | Host Code | Host Demo | Live Link Example |
|---|---|---|---|
| HTML/CSS/JS Web | GitHub | GitHub Pages | `yogesh1300.github.io/project` |
| Flask/Django | GitHub | Render | `project-xxxxx.onrender.com` |
| React App | GitHub | Vercel | `project.vercel.app` |
| Rasa Chatbot | GitHub | Hugging Face Spaces | `huggingface.co/spaces/...` |
| Python ML/Data | GitHub | Streamlit Cloud | `yogesh-project.streamlit.app` |
| Arduino/IoT | GitHub | GitHub (docs) | `github.com/yogesh1300/project` |

---

## SUMMARY

**When Complete, Your Portfolio Will:**

✅ Display 6+ live working projects
✅ Show project screenshots
✅ Link to GitHub source code
✅ Have clickable live demos
✅ Be accessible at `https://yogesh1300.github.io`
✅ Look professional for recruiters & seniors
✅ Showcase your full skill set
✅ Be easy to update with new projects

**Estimated Time: 2-3 weeks** (depending on project complexity)

---

**Next Steps:**
1. Start with Step 1.1 (list your projects)
2. Follow each phase in order
3. Test thoroughly before sharing
4. Share portfolio link widely!

Good luck! 🚀
