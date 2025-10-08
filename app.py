# app.py — Modern Streamlit Portfolio for Jino Mathew (Animated & Mobile-Friendly Edition)

import streamlit as st
import pandas as pd
import os
import json
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Jino Mathew | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------- THEME & GLOBAL STYLES ----------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    :root {
        --primary: #3B82F6;  
        --accent:  #14B8A6;  
        --bg:      #0D1117;  
        --text:    #E6E6E6;  
        --muted:   #9CA3AF;  
        --card:    #111827;  
        --border:  #1F2937;  
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, var(--bg) 0%, #0A0F1C 100%);
        color: var(--text);
        font-family: 'Inter', sans-serif;
        padding-left: 10px;
        padding-right: 10px;
    }
    #MainMenu, footer { visibility: hidden; }

    @keyframes fadeUp { from {opacity: 0; transform: translateY(20px);} to {opacity: 1; transform: translateY(0);} }
    @keyframes shimmer { 0% {background-position: -200% center;} 100% {background-position: 200% center;} }

    .card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 16px 18px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.35);
        animation: fadeUp 0.6s ease-out;
        transition: transform .3s ease, box-shadow .3s ease;
        width: 100%;
    }
    .card:hover { transform: translateY(-3px); box-shadow: 0 10px 24px rgba(0,0,0,0.45); }

    .chip {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 999px;
        background: rgba(79,70,229,0.12);
        border: 1px solid rgba(79,70,229,0.35);
        color: var(--text);
        font-size: 12px;
        margin: 4px 6px 0 0;
        backdrop-filter: blur(6px);
        transition: all .2s ease;
    }
    .chip:hover { background: rgba(79,70,229,0.25); transform: scale(1.05); }

    .pill {
        padding: 5px 8px;
        border-radius: 999px;
        font-size: 11px;
        color: var(--text);
        background: rgba(255,255,255,0.04);
        border: 1px solid var(--border);
        margin-right: 5px;
        transition: all .2s ease;
    }
    .pill:hover { background: rgba(20,184,166,0.15); border-color: var(--accent); }

    .h1 { font-size: 28px; font-weight: 700; margin: 0 0 6px 0; }
    .h2 { font-size: 20px; font-weight: 600; margin: 0 0 12px 0; }
    .muted { color: var(--muted); }
    .divider { height: 1px; background: var(--border); width: 100%; margin: 8px 0 12px 0; }

    .tagline {
        background: linear-gradient(90deg, var(--primary), var(--accent), var(--primary));
        background-size: 200%;
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-weight: 600;
        letter-spacing: 0.02em;
        animation: shimmer 5s infinite linear;
    }

    .social a { text-decoration: none; margin-right: 8px; }
    .social .btn {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(31,41,55,0.6);
        border: 1px solid var(--border);
        color: var(--text);
        padding: 6px 10px; border-radius: 8px; font-size: 12px;
        transition: all .25s ease;
    }
    .social .btn:hover { border-color: var(--accent); box-shadow: 0 0 10px rgba(20,184,166,0.25); transform: scale(1.05); }

    .resume-btn { color: #ffffff !important; background-color: #4B5563 !important; }
    .resume-btn:hover { background-color: #1F2937 !important; }

    /* Desktop fixed profile card */
    @media (min-width: 1200px) { .profile-fixed { position: fixed; right: 24px; top: 88px; width: 280px; } }

    /* Tablet adjustments */
    @media (max-width: 1200px) {
        .profile-fixed { position: relative; width: 100%; margin-top: 20px; }
        .h1 { font-size: 24px; }
        .h2 { font-size: 18px; }
    }

    /* Mobile adjustments & stacked columns */
    @media (max-width: 768px) {
        .h1 { font-size: 20px; }
        .h2 { font-size: 16px; }
        .chip { font-size: 10px; padding: 4px 8px; }
        .pill { font-size: 10px; padding: 4px 6px; }
        .social .btn { padding: 4px 8px; font-size: 11px; gap: 4px; }

        /* Stack left/right columns vertically */
        .stColumns > div { width: 100% !important; display: block !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- HEADER ----------------
header_col1, header_col2 = st.columns([0.65, 0.35], gap="large")

with header_col1:
    st.markdown('<div class="h1">Jino Mathew M J</div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">Data Analyst •  Analytics Storyteller</div>', unsafe_allow_html=True)
    st.markdown('<div class="muted" style="margin-top:8px;">I transform raw data into meaningful insights and actionable business narratives through effective analysis, statistical methods, and visually compelling Power BI dashboards.</div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="social">
          <a href="mailto:jinomathew2105@gmail.com" target="_blank"><span class="btn">📧 Email</span></a>
          <a href="https://www.linkedin.com/in/jino-mathew-2a6177221/" target="_blank"><span class="btn">🔗 LinkedIn</span></a>
          <a href="https://github.com/Jingi2103" target="_blank"><span class="btn">💻 GitHub</span></a>
          <a href="https://medium.com/@jinomathew2105" target="_blank"><span class="btn">🌐 MEDIUM</span></a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    try:
        with open("assets/data_animation.json", "r") as f:
            lottie_data = json.load(f)
    except:
        pass

with header_col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    img_path = "profile.jpg"
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True, caption="Jino Mathew")
    else:
        st.image("assets/profile.png", use_container_width=True, caption="Profile Picture")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# ---------------- FULL-WIDTH RESPONSIVE TIMELINE ----------------
st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

timeline_data = pd.DataFrame({
    "Year": [2022, 2024, 2024, 2024, 2025],
    "Milestone": [
        "🎓 BCA (Kristu Jayanti College)",
        "🎓 MSc Data Science (Christ-Deemed to be University)",
        "💻 Full Stack Developer Intern (Unizen Technologies)",
        "👨‍🏫 Assistant Professor at (Koshy’s Group of Institution)",
        "📊 Data Analyst(Diya Ghar)"
    ],
    "Category": ["Education", "Education", "Internship", "Work Experience", "Work Experience"],
    "YOffset": [0, 0.05, 0.3, 0.45, 0.6]
})
timeline_data["YOffset_responsive"] = timeline_data["YOffset"] * 0.6

category_colors = {
    "Education": "#4F46E5",
    "Internship": "#FCD392",
    "Work Experience": "#10B981"
}

fig = go.Figure()
for category, color in category_colors.items():
    cat_data = timeline_data[timeline_data["Category"] == category]
    fig.add_trace(go.Scatter(
        x=cat_data["Year"],
        y=cat_data["YOffset_responsive"],
        mode="markers",
        name=category,
        marker=dict(size=12, color=color, line=dict(width=2, color="#0D0D0D")),
        text=cat_data["Milestone"],
        textposition="top center",
        hovertemplate="<b>%{text}</b><br>Year: %{x}<br>Category: " + category
    ))

frames = [
    go.Frame(
        data=[
            go.Scatter(
                x=timeline_data["Year"][:i],
                y=timeline_data["YOffset_responsive"][:i],
                mode="lines+markers+text",
                line=dict(color="#14B8A6", width=3),
                marker=dict(size=12, color=[category_colors[c] for c in timeline_data["Category"][:i]], line=dict(width=2, color="#0D0D0D")),
                text=timeline_data["Milestone"][:i],
                textposition="top center",
                hovertemplate="<b>%{text}</b><br>Year: %{x}<br>Category: %{customdata}",
                customdata=timeline_data["Category"][:i]
            )
        ]
    )
    for i in range(1, len(timeline_data) + 1)
]
fig.frames = frames

fig.update_layout(
    autosize=True,
    height=400,
    margin=dict(l=20, r=20, t=50, b=50),
    title=dict(text="📈 Education, Internship & Work Experience Timeline", font=dict(size=18, color="white")),
    font=dict(color="#FF69b4"),
    xaxis=dict(tickvals=[2022, 2024, 2025], ticktext=["2022", "2024", "2025"], showgrid=False, zeroline=False, tickfont=dict(size=11)),
    yaxis=dict(visible=False),
    hovermode="closest",
    legend=dict(orientation="v", yanchor="top", y=0.95, xanchor="left", x=1.05, font=dict(color="#E5A0d7", size=11)),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    updatemenus=[{
        "type": "buttons",
        "showactive": False,
        "buttons": [{
            "label": "▶ View Career Roadmap",
            "method": "animate",
            "args": [None, {"frame": {"duration": 800, "redraw": True}, "fromcurrent": True, "mode": "immediate"}]
        }],
        "x": 0.42, "y": -0.12
    }]
)
st.plotly_chart(fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- MAIN LAYOUT ----------------
left, right = st.columns([0.62, 0.38], gap="large")

with left:
    # About Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="h2">About</div>', unsafe_allow_html=True)
    st.write(
        "I’m a Data Science graduate with hands-on experience as a data analyst in the Monitoring & Evaluation (M&E) team. Skilled in Python, R, SQL, Excel, and Power BI, I focus on transforming complex datasets into actionable insights that drive program performance and strategic decisions. "
        "My work involves data cleaning, visualization, statistical analysis and indicator tracking to ensure accuracy, accountability, and outcome-based evaluation."
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Skills
    st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="h2">Skills</div>', unsafe_allow_html=True)
    skills = [
        "Python", "SQL", "R Programming", "Pandas", "Numpy", "Seaborn", "Scikit-learn", "Matplotlib", "Plotly",
        "Streamlit", "Power BI",  "Advance Excel", "AWS", "Data Cleaning", "Data Processing", "Data Visualization",
        "Descriptive & Inferential Statistics", "Monitoring and Evaluation concepts", "Analytical storytelling "
    ]
    st.markdown("".join(['<span class="chip">' + s + "</span>" for s in skills]), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Projects
    st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="h2">Projects</div>', unsafe_allow_html=True)

    def project(title, desc, tags, link=None):
        st.markdown('<div style="margin-bottom:14px;">', unsafe_allow_html=True)
        st.markdown(f'<div style="font-weight:600;">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="muted" style="margin:6px 0 8px 0;">{desc}</div>', unsafe_allow_html=True)
        st.markdown("".join(['<span class="pill">' + t + "</span>" for t in tags]), unsafe_allow_html=True)
        if link:
            st.markdown(f'<div style="margin-top:8px;"><a href="{link}" target="_blank">🔎 View</a></div>', unsafe_allow_html=True)
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    project(
        "Asia cup 2025 prediction -- Cricket analysis",
        "A Python-based simulation to track the probability of each Super-4 team (India, Pakistan, Sri Lanka, Bangladesh) winning the Asia Cup 2025. Monte Carlo simulations are used to estimate title-winning probabilities and generate charts showing probability trends over time.",
        ["Python", "Matplotlib", "Numpy", "Google colab", "Monte Carlo Simulation"],
        "https://github.com/Jingi2103/Asia-Cup-2025---Cricket-Analysis",
    )
    project(
        "Student performance analysis -- using T-test",
        "Analysis of student performance using T-test and graphs.",
        ["Python", "Matplotlib", "Numpy", "Pandas", "Scipy","Google colab", "T-test", "Statistical Analysis"],
        "https://github.com/Jingi2103/Student-performance-analysis",
    )
    project(
        "Indian Sign Language to Text Conversion",
        "A real-time web app that converts Indian Sign Language gestures into text using LSTM and MediaPipe.",
        ["Python", "TensorFlow", "OpenCV", "Streamlit"],
        "https://github.com/Jingi2103/Indian-Sign-Language-to-Text-Conversion-A-Real-Time-Web-App",
    )
    project(
        "Points Table Web App for a football Tournament",
        "Built a Streamlit-based app to dynamically display team rankings and match results from Excel sheets.",
        ["Streamlit", "Python", "Excel"],
    )
    project(
        "Aqua Count: Smart Water Meter",
        "A web application for smart water monitoring built during Full Stack Internship at Unizen Technologies.",
        ["Node.js", "JavaScript", "HTML/CSS"],
    )
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    # Contact + Resume Download
    st.markdown('<div class="card profile-fixed">', unsafe_allow_html=True)
    st.markdown('<div class="h2">Contact</div>', unsafe_allow_html=True)
    st.markdown("- 📍 Bangalore, India")
    st.markdown("- ✉️ jinomathew2105@gmail.com")
    st.markdown("- 🔗 https://www.linkedin.com/in/jino-mathew-2a6177221/")

    resume_path = "resume.pdf"
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as pdf_file:
            st.markdown(
                """
                <style>
                div[data-testid="stDownloadButton"] > button {
                    background-color: #6B7280; color: white; border: none;
                    border-radius: 8px; padding: 8px 18px; font-weight: 500;
                    transition: background-color 0.3s ease;
                }
                div[data-testid="stDownloadButton"] > button:hover { background-color: #1F2937; color: white; }
                </style>
                """,
                unsafe_allow_html=True
            )
            st.download_button(
                label="📄 Download Resume",
                data=pdf_file.read(),
                file_name="resume.pdf",
                mime="application/pdf",
                key="resume_btn"
            )
    else:
        st.error("⚠️ Resume file not found. Please place 'resume.pdf' in your app folder.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Highlights
    st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="h2">Highlights</div>', unsafe_allow_html=True)
    st.markdown("- Built statistical models and Data Science projects")
    st.markdown("- Experienced in analytics, teaching, and full stack development")
    st.markdown("- Passionate about coding, meaningful data, and innovation ")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
st.markdown(
    f'<div style="text-align:center; color:#9CA3AF; font-size: 13px;">© {pd.Timestamp.now().year} Jino Mathew • Built with ❤️ & Streamlit</div>',
    unsafe_allow_html=True,
)
