import streamlit as st
import pandas as pd
import re
from backend import process_server

st.set_page_config(page_title="DevOps Tool", layout="centered")

st.title("🚀 User Management Tool")

# Action dropdown
action = st.selectbox("Select Action", ["create", "delete"])

# File upload
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "csv"])


# 🔍 Validation function
def validate_file(df):
    errors = []

    # Empty check
    if df.empty:
        errors.append("File is empty")

    # Required columns
    required_cols = ["ip", "username"]
    for col in required_cols:
        if col not in df.columns:
            errors.append(f"Missing column: {col}")

    # IP + username validation
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

    for i, row in df.iterrows():
        ip = str(row.get("ip", "")).strip()
        user = str(row.get("username", "")).strip()

        if not re.match(ip_pattern, ip):
            errors.append(f"Invalid IP at row {i+1}: {ip}")

        if user == "":
            errors.append(f"Missing username at row {i+1}")

    # Duplicate IP check
    if "ip" in df.columns and df["ip"].duplicated().any():
        errors.append("Duplicate IPs found")

    return errors


# Main logic
if uploaded_file:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📄 Uploaded Data")
    st.dataframe(df)

    # Validate
    errors = validate_file(df)

    if errors:
        st.error("❌ Validation Failed")
        for err in errors:
            st.write(err)

    else:
        st.success("✅ File validation passed")

        if st.button("Run"):

            ssh_user = "ec2-user"   # SSH login user
            key_path = "tf-key.pem"

            st.info("⏳ Running automation...")

            results = []

            for _, row in df.iterrows():
                ip = row["ip"]
                target_user = row["username"]

                output = process_server(ip, ssh_user, key_path, target_user, action)
                results.append(output)

            st.success("✅ Execution Completed")

            st.subheader("📊 Results")
            for r in results:
                st.text(r)