import streamlit as st
from style import local_css
import streamlit.components.v1 as components

def js_alert(text):
    components.html(f"""
    <script>
    alert("{text}");
    </script>
    """, height=0)


st.set_page_config(page_title="แอปมังงะ", layout="centered")
local_css()

st.markdown("<h1 style='text-align: center;'>ร้านหนังสือ</h1>", unsafe_allow_html=True)

st.image('https://jumpg-assets.tokyo-cdn.com/secure/top_banner/229470.jpg?hash=iBo8Yt11X_GmJId9I0GaNw&expires=2145884400')

st.markdown("<h2 style='text-align: center;'>เกี่ยวกับเรา</h2>", unsafe_allow_html=True)
st.success("ร้านหนังสือของเรามีหนังสือหลากหลายประเภท ตั้งแต่หนังสือเรียน หนังสือนิยาย ไปจนถึงหนังสือวิชาการ")

st.video('https://youtu.be/U-YIvbMWDDw?si=6O6ZA0Ot0KCIz0N8')

st.markdown("<h2 style='text-align: center;'>สินค้าของเรา</h2>", unsafe_allow_html=True)

books = [
    {"title": "Drama Queen", "img": "https://jumpg-assets.tokyo-cdn.com/secure/title/100404/title_thumbnail_portrait_list/386681.jpg?hash=4Y2-u5mBYmgOCtLqvWo9Rw&expires=2145884400"},
    {"title": "Strikeout Pitch", "img": "https://jumpg-assets.tokyo-cdn.com/secure/title/100345/title_thumbnail_portrait_list/370171.jpg?hash=OZzoCA7S6HdgqHAs-LQ-WA&expires=2145884400"},
    {"title": "Ichi the Witch", "img": "https://jumpg-assets.tokyo-cdn.com/secure/title/100348/title_thumbnail_portrait_list/371494.jpg?hash=532nnlAxLgYd4wc2IyxxLA&expires=2145884400"},
    {"title": "RuriDragon", "img": "https://jumpg-assets.tokyo-cdn.com/secure/title/100196/title_thumbnail_portrait_list/313570.jpg?hash=rx4_NfijYDvzGCvOIlkmTQ&expires=2145884400"},
    {"title": "Blue Exorcist", "img": "https://jumpg-assets.tokyo-cdn.com/secure/title/100005/title_thumbnail_portrait_list/311848.jpg?hash=h2hrMHKi-kJCkbbpuBQG0Q&expires=2145884400"},
    {"title": "Gokurakugai", "img": "https://jumpg-assets.tokyo-cdn.com/secure/title/100230/title_thumbnail_portrait_list/312550.jpg?hash=NWVyhTI-xUOA_RHSK1pXhg&expires=2145884400"}
]


if 'cart' not in st.session_state:
    st.session_state.cart = []


def add_to_cart(book_title):
    st.session_state.cart.append(book_title)
    st.success(f"เพิ่ม '{book_title}' ลงตะกร้าเรียบร้อยแล้ว")

for i in range(0, len(books), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(books):
            with cols[j]:
                book = books[i + j]
                st.markdown(f"<h5 style='text-align: center;'>{book['title']} เล่ม 1</h5>", unsafe_allow_html=True)
                st.image(book['img'])
                st.markdown(f"<h3 style='text-align: center;'>{book['title']}</h3>", unsafe_allow_html=True)
                st.button('ราคา 160 บาท', type='primary', use_container_width=True, key=f"book_price_{i+j}")
                if st.button('เพิ่มลงตระกร้า', use_container_width=True, key=f"book_add_{i+j}"):
                    add_to_cart(book['title'])

col1, col2 = st.columns(2)
with col1:
    st.button('หน้าก่อนหน้า', type='primary', use_container_width=True, key='btn_prev')
with col2:
    st.button('หน้าถัดไป', type='primary', use_container_width=True, key='btn_next')

# แสดงตะกร้าสินค้า
st.markdown("<h2 style='text-align: center;'>ตะกร้าสินค้า</h2>", unsafe_allow_html=True)
if st.session_state.cart:
    for idx, item in enumerate(st.session_state.cart, 1):
        st.markdown(f"{idx}. {item}")
else:
    st.info("ตะกร้ายังว่างอยู่")

# รีวิวลูกค้า
st.markdown("<h2 style='text-align: center;'>รีวิวลูกค้า</h2>", unsafe_allow_html=True)

star = st.slider(label='จำนวนดาว', min_value=1, max_value=5, value=3, step=1, key='star_rating')

# กำหนดสีข้อความตามจำนวนดาว
color_dict = {
    1: "red",
    2: "orangered",
    3: "orange",
    4: "yellowgreen",
    5: "green"
}
star_color = color_dict.get(star, "black")

st.markdown(f"<p style='text-align: center; font-size: 30px; color:{star_color};'>{'⭐' * star}</p>", unsafe_allow_html=True)

text_review = st.text_input(label='รีวิวลูกค้า', placeholder='เขียนรีวิวของคุณ')
btn_submit = st.button('ส่งรีวิว', use_container_width=True, key='btn_submit1')
if btn_submit:
    if text_review:
        st.success(f"<span style='color:{star_color}'>{text_review}</span>", unsafe_allow_html=True)
    else:
        st.error('กรุณากรอกรีวิวก่อนส่ง')
