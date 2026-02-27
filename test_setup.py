import sys
print(f"✅ Python version: {sys.version}")

try:
    import pandas as pd
    print("✅ Pandas installed")
except ImportError:
    print("❌ Pandas not installed")

try:
    import selenium
    print("✅ Selenium installed")
except ImportError:
    print("❌ Selenium not installed")

try:
    import google.generativeai as genai
    print("✅ Gemini AI installed")
except ImportError:
    print("❌ Gemini AI not installed")

try:
    import streamlit as st
    print("✅ Streamlit installed")
except ImportError:
    print("❌ Streamlit not installed")

print("\n🎉 Setup complete! Ready to start coding.")