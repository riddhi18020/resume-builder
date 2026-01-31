import streamlit as st
from fpdf import FPDF

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Resume Builder", layout="centered")
st.title("📄 Resume Builder ")

# ------------------ PDF CLASS ------------------
class ResumePDF(FPDF):

    def header(self):
        self.set_font("Helvetica", "B", 18)
        self.cell(0, 10, "RESUME", ln=True, align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def section_body(self, text):
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 8, text)
        self.ln(2)


# ------------------ FORM ------------------
with st.form("resume_form"):

    st.subheader("👤 Personal Information")

    name = st.text_input("Full Name *")
    gender = st.radio("Gender *", ["Male", "Female", "Other"])
    email = st.text_input("Email *")
    phone = st.text_input("Contact Number *")
    address = st.text_area("Address *")

    st.subheader("🌐 Social Profiles")
    linkedin = st.text_input("LinkedIn Profile *")
    github = st.text_input("GitHub Profile *")

    st.subheader("🎓 Education")
    college = st.text_input("College / University Name *")

    degree = st.selectbox("Degree *", ["Under Graduation", "Post Graduation"])

    if degree == "Under Graduation":
        year = st.radio("Year *", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
    else:
        year = st.radio("Year *", ["1st Year", "2nd Year"])

    st.subheader("💻 Skills & Experience")

    technical_skills = st.text_area("Technical Skills *", max_chars=10000)
    experience = st.text_area("Professional Experience (Optional)", max_chars=10000)

    st.subheader("🎯 Career")
    career_goal = st.text_area("Career Goal *")
    strength = st.text_area("Strength *")

    submit = st.form_submit_button("✅ Generate Resume")


# ------------------ FORM VALIDATION ------------------
if submit:

    if not all([name, email, phone, address, linkedin, github, college,
                technical_skills, career_goal, strength]):
        st.error("❌ Please fill all mandatory fields!")
        st.stop()

    # ------------------ CREATE PDF ------------------
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.section_title("Personal Information")
    pdf.section_body(
        f"Name: {name}\nGender: {gender}\nEmail: {email}\n"
        f"Phone: {phone}\nAddress: {address}"
    )

    pdf.section_title("Social Profiles")
    pdf.section_body(f"LinkedIn: {linkedin}\nGitHub: {github}")

    pdf.section_title("Education")
    pdf.section_body(f"College: {college}\nDegree: {degree}\nYear: {year}")

    pdf.section_title("Technical Skills")
    pdf.section_body(technical_skills)

    if experience:
        pdf.section_title("Professional Experience")
        pdf.section_body(experience)

    pdf.section_title("Career Goal")
    pdf.section_body(career_goal)

    pdf.section_title("Strength")
    pdf.section_body(strength)

    pdf.output("resume.pdf")

    with open("resume.pdf", "rb") as f:
        st.download_button("⬇️ Download Resume PDF", f, "My_Resume.pdf")

    st.success("🎉 Resume Generated Successfully!")
