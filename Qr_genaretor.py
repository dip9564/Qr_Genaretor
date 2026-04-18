from io import BytesIO
import qrcode as qr
import streamlit as st

# SIDEBAR
with st.sidebar:
    st.subheader("ℹ️ About this app")
    st.write("👨‍💻 Created by **Dip Mondal**")
    st.write(
        "This is a simple QR Code Generator built using **Streamlit**. "
        "You can generate QR codes for any text or URL."
    )
    st.markdown("---")
    st.markdown("### 📌 How to use")
    st.markdown("""
    1. Enter text or URL  
    2. Click **Generate QR Code**  
    3. Download the QR image  
    """)
    st.markdown("---")
    st.info("💡 You can use this QR for websites, text, or sharing links.")
# main app
st.title('📱 QR Generator')
st.write("Generate QR codes from text or URL")
url=st.text_input('Enter text')

name=st.text_input('Enter filename ','qr.png')

if st.button("Generate"):
    if url:
        img = qr.make(url)
        
        buf = BytesIO()
        img.save(buf)
        buf.seek(0)
        st.image(buf.getvalue(),width=300)

        st.download_button(
            label="Download QR",
            data=buf.getvalue(),
            file_name=name if name.endswith('.png') else name + '.png',
            mime="image/png"
        )

    else:
        st.warning("Please enter some text")

