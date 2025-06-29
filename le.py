import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="البحث من ملف Excel", layout="centered")
st.title("🔍 البحث عن بيانات المستخدم")

# اسم الملف والعمود
EXCEL_FILE = "year1.xlsx"
COLUMN_NAME = "num"

try:
    # تحميل الملف
    df = pd.read_excel(EXCEL_FILE)
    st.success(f"✅ تم تحميل الملف بنجاح. سيتم البحث في العمود '{COLUMN_NAME}'.")

    if COLUMN_NAME not in df.columns:
        st.error(f"❌ العمود '{COLUMN_NAME}' غير موجود في الملف.")
    else:
        # إدخال الرقم
        user_input = st.text_input("🔢 أدخل الرقم المطلوب:")

        if user_input:
            try:
                user_input = pd.to_numeric(user_input, errors="coerce")
            except:
                pass

            # البحث عن الصف
            result = df[df[COLUMN_NAME] == user_input]

            if not result.empty:
                st.success("✅ تم العثور على البيانات التالية:")

                # عرض بيانات الصف كسطور منفصلة
                row = result.iloc[0]  # أول صف مطابق
                for col, value in row.items():
                    st.write(f"**{col}**: {value}")

            else:
                st.warning("⚠️ لم يتم العثور على الرقم.")

except FileNotFoundError:
    st.error(f"❌ لم يتم العثور على الملف '{EXCEL_FILE}'.")
except Exception as e:
    st.error(f"❌ حدث خطأ أثناء التنفيذ: {e}")
