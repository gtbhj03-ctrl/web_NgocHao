import streamlit as st
import os

# Cấu hình giao diện trang web hiển thị rộng rãi, đẹp mắt
st.set_page_config(page_title="Sổ Tay Học Tập Của Ngọc Hào", page_icon="📚", layout="wide")

st.title("📚 Hệ Thống Lưu Trữ Công Thức & Từ Vựng Của Ngọc Hào")
st.write("Ứng dụng chạy tự động giúp tra cứu nhanh công thức Toán, cấu trúc Tiếng Anh và các file tài liệu đính kèm.")

DATA_FILE = "sotay_data.txt"

# --- [DỮ LIỆU ĐƯỢC CHÈN SẴN THEO YÊU CẦU - KHÔNG BỎ SÓT] ---
FILE_1_CONTENT = "KSKS {vql }xsnid_Z }xsnid_Z }xsnid_Z {vqlg }xsnid_Z }xsnid_Z }xsnid_Z |wrmhc^Y }xsnid_Z }xsnid_Z }xsnid_Z }xsnid_Z  & 6"[cite: 1]

FILE_2_CONTENT = """Các cấu trúc câu cơ bản và thông dụng được sử dụng nhiều trong tiếng Anh
1. S + V + too + adj/adv + (for someone) + to do something: ( quá….để cho ai làm gì…)
e.g. This structure is too easy for you to remember. ( Cấu trúc này quá dễ cho bạn để nhớ )        He ran too fast for me to follow. (Anh ấy chạy quá nhanh để tôi kịp theo) 
2. S + V + so + adj/ adv + that + S + V: ( quá… đến nỗi mà… )
e.g. This box is so heavy that I cannot take it. (Chiếc hộp này quá nặng đến nỗi tôi không thể mang nó lên được)
e.g. He speaks so soft that we can’t hear anything. (Anh ấy nói quá nhỏ đến nỗi chúng tôi không thể nghe được gì)
3. It + V + such + (a/an) + N(s) + that + S + V: ( quá… đến nỗi mà… )
e.g. It is such a heavy box that I cannot take it. (Chiếc hộp này quá nặng đến nỗi tôi không thể mang nó lên được)
e.g. It is such interesting books that I cannot ignore them at all. (Những cuốn sách này quá thú vị đến nỗi mà tối không thể phớt lờ chúng được)
4. S + V + adj/ adv + enough + (for someone) + to do something : ( Đủ… cho ai đó làm gì… )
e.g. She is old enough to get married. (Cô ấy đã đủ tuổi để kết hôn)
e.g. They are intelligent enough for me to teach them English. (Họ đủ thông minh để tôi dạy tiếng anh cho họ)
5. Have/ get + something + done (past participle): ( nhờ ai hoặc thuê ai làm gì… )
e.g. I had my hair cut yesterday. (Tôi cắt tóc hôm qua)
6. It + be + time + S + V (-ed, cột 2) / It’s +time +for someone +to do something : ( đã đến lúc ai đó phải làm gì… )
e.g. It is time you had a shower. (Đã đến lúc bạn đi tắm)
e.g. It’s time for me to ask all of you for this question. (Đã đến lúc tôi hỏi bạn câu hỏi này)
7. It + takes/took+ someone + amount of time + to do something:( làm gì…mất bao nhiêu thời gian…)
e.g. It takes me 5 minutes to get to school. (Tôi mất 5 phút để đi học)
e.g. It took him 10 minutes to do this exercise yesterday. (Anh ấy mất 10 phút để làm bài tập ngày hôm qua)
8. To prevent/stop + someone/something + From + V-ing: ( ngăn cản ai/ cái gì… làm gì.. )
e.g. He prevented us from parking our car here. (Anh ấy ngăn họ không được đỗ xe tại đây)
9. S + find+ it+ adj to do something: ( thấy … để làm gì… )
e.g. I find it very difficult to learn about English. (Tôi thấy quá khoe để học tiếng anh)
e.g. They found it easy to overcome that problem. (Họ thấy vấn đề này quá dễ để vượt qua)
10. To prefer + Noun/ V-ing + to + N/ V-ing. ( Thích cái gì/ làm gì hơn cái gì/ làm gì )
e.g. I prefer dog to cat. (Tôi thích chó hơn mèo) 
e.g. I prefer reading books to watching TV. (Tôi thích đọc sách hơn xem TV)
11. Would rather (‘d rather) + V (infinitive) + than + V (infinitive: ( thích làm gì hơn làm gì )
e.g. She would play games than read books. (Cô ấy thích chơi điện tử hơn đọc sách)
e.g. I’d rather learn English than learn Biology. (Tôi thích học Tiếng anh hơn môn sinh học)
12. To be/get Used to + V-ing: ( quen làm gì )
e.g. I am used to eating with chopsticks. (Tôi quen với việc dùng đũa để ăn)
13. Used to + V (infinitive): ( Thường làm gì trong qk và bây giờ không làm nữa )
e.g. I used to go fishing with my friend when I was young. (Tôi từng đi câu cá với bạn khi tôi còn trẻ)
e.g. She used to smoke 10 cigarettes a day. (Cô ấy tường hút 10 điếu xì gà 1 ngày)
14. To be amazed at = to be surprised at + N/V-ing: ( ngạc nhiên về… )
e.g. I was amazed at his big beautiful villa. (Tôi rất ngạc nhiên về căn biệt thự rất đẹp của anh ấy)
15. To be angry at + N/V-ing: ( tức giận về )
e.g. Her mother was very angry at her bad marks. (Mẹ cô ấy đã rất tức giận về những điểm kém của cô ấy)
16. to be good at/ bad at + N/ V-ing: ( giỏi về…/ kém về… )
e.g. I am good at swimming. (Tôi bơi rất giỏi)
e.g. He is very bad at English. (Anh ấy rất kém về tiếng Anh)
17. by chance = by accident (adv): ( tình cờ )
e.g. I met her in Paris by chance last week. (Tôi tình cờ gặp cô ấy tại Pari tuần trước)
18. to be/get tired of + N/V-ing: ( mệt mỏi về… )
e.g. My mother was tired of doing too much housework everyday. (Mẹ tôi quá mệt mỏi vì việc nhà mỗi ngày)
19. can’t stand/ help/ bear/ resist + V-ing: ( Không chịu nỗi/không nhịn được làm gì… )
e.g. She can’t stand laughing at her little dog. (Cô ấy không thể nhịn cười với con chó của cô ấy)
20. to be keen on/ to be fond of + N/V-ing : ( thích làm gì đó… )
e.g. My younger sister is fond of playing with her dolls. (Em gái tôi thích chơi búp bê)
21. to be interested in + N/V-ing: ( quan tâm đến… )
e.g. Mrs Brown is interested in going shopping on Sundays. (Bà Brown quan tâm đến việc đi mua sắm vào mỗi Chủ nhật)
22. to waste + time/ money + V-ing: ( tốn tiền hoặc thời gian làm gì )
e.g. He always wastes time playing computer games each day. (Anh ấy luôn tốn thời gian dể chơi điện tử mỗi ngày)
e.g. Sometimes, I waste a lot of money buying clothes. (Thỉnh thoảng, tôi tiêu tốn tiền bạc vào việc mua quần áo)
23. To spend + amount of time/ money + V-ing: ( dành bao nhiêu thời gian/ tiền bạc làm gì…)
e.g. I spend 2 hours reading books a day. (Tôi dành 2 giờ để đọc sách mỗi ngày)
e.g. Mr Jim spent a lot of money traveling around the world last year.(Ngài Jim dành nhiều tiền vào việc đi du lịch vòng quanh Thế giới vào năm ngoái)
24. To spend + amount of time/ money + on + something: ( dành thời gian/tiền bạc vào việc gì… )
e.g. My mother often spends 2 hours on housework everyday. (Mẹ tối dành 2 giờ mỗi ngày để làm việc nhà)
e.g. She spent all of her money on clothes. (Cô ấy dành tất cả tiền vào quần áo)
25. to give up + V-ing/ N: ( từ bỏ làm gì/ cái gì… )
e.g. You should give up smoking as soon as possible. (Bạn nên từ bỏ việc hút thuốc sớm nhất có thể)
26. would like/ want/wish + to do something: ( thích làm gì… )
e.g. I would like to go to the cinema with you tonight. (Tôi thích đi xem phim với bạn tối nay)
27. have + (something) to + Verb: ( có cái gì đó để làm )
e.g. I have many things to do this week. (Tôi có nhiều việc để làm trong tuần này)
28. It + be + something/ someone + that/ who: ( chính…mà… )
e.g. It is Tom who got the best marks in my class. (Đó chính là Tom người có nhiều điểm cao nhất lớp tôi)
e.g. It is the villa that he had to spend a lot of money last year. (Đó chính là biệt thự mà anh ấy dành tiền để mua năm ngoái)
29. Had better + V(infinitive): ( nên làm gì… ).
e.g. You had better go to see the doctor. (bạn nên đến gặp bác sĩ)
30. hate/ like/ dislike/ enjoy/ avoid/ finish/ mind/ postpone/ practise/ consider/ delay/ deny/ suggest/ risk/ keep/ imagine/ fancy + V-ing
e.g. I always practise speaking English everyday. (Tôi luôn thực hành nói tiếng anh mỗi ngày)
31. It is + tính từ + ( for smb ) + to do smt : ( khó để làm gì )
e.g. It is difficult for old people to learn English. (Người có tuổi học tiếng Anh thì khó)
32. To be interested in + N / V_ing ( Thích cái gì / làm cái gì )
e.g. We are interested in reading books on history. (Chúng tôi thích đọc sách về lịch sử)
33. To be bored with ( Chán làm cái gì )
e.g. We are bored with doing the same things everyday. (Chúng tôi chán ngày nào cũng làm những công việc lặp đi lặp lại)
34. It’s the first time smb have ( has ) + PII smt ( Đây là lần đầu tiên ai làm cái gì )
e.g. It’s the first time we have visited this place. (Đây là lần đầu tiên chúng tôi tới thăm nơi này)
35. enough + danh từ ( đủ cái gì ) + ( to do smt )
e.g. I don’t have enough time to study. (Tôi không có đủ thời gian để học)
36. Tính từ + enough (đủ làm sao ) + ( to do smt )
e.g. I’m not rich enough to buy a car. (Tôi không đủ giàu để mua ôtô)
37. too + tính từ + to do smt ( Quá làm sao để làm cái gì )
e.g. I’m to young to get married. (Tôi còn quá trẻ để kết hôn)
38. To want smb to do smt = To want to have smt + PII(Muốn ai làm gì ) ( Muốn có cái gì được làm )
e.g. She wants someone to make her a dress. (Cô ấy muốn ai đó may cho cô ấy một chiếc váy)
= She wants to have a dress made. (Cô ấy muốn có một chiếc váy được may)
39. It’s time smb did smt ( Đã đến lúc ai phải làm gì )
e.g. It’s time we went home. (Đã đến lúc tôi phải về nhà)
40. It’s not necessary for smb to do smt = Smb don’t need to do smt(Ai không cần thiết phải làm gì ) doesn’t have to do smt
e.g. It is not necessary for you to do this exercise. (Bạn không cần phải làm bài tập này)
41. To look forward to V_ing ( Mong chờ, mong đợi làm gì )
e.g. We are looking forward to going on holiday. (Chúng tôi đang mong được đi nghỉ)
42. To provide smb with V_ing ( Cung cấp cho ai cái gì )
e.g. Can you provide us with some books in history? (Bạn có thể cung cấp cho chúng tôi một số sách về lịch sử không?)
43. To prevent smb from V_ing (Cản trở ai làm gì )To stop
e.g. The rain stopped us from going for a walk. (Cơn mưa đã ngăn cản chúng tôi đi dạo)
44. To fail to do smt (Không làm được cái gì / Thất bại trong việc làm cái gì)
e.g. We failed to do this exercise. (Chúng tôi không thể làm bài tập này)
45. To be succeed in V_ing (Thành công trong việc làm cái gì)
e.g. We were succeed in passing the exam. (Chúng tôi đã thi đỗ)
46. To borrow smt from smb (Mượn cái gì của ai)
e.g. She borrowed this book from the library. (Cô ấy đã mượn cuốn sách này ở thư viện)
47. To lend smb smt (Cho ai mượn cái gì)
e.g. Can you lend me some money? (Bạn có thể cho tôi vay ít tiền không?)
48. To make smb do smt (Bắt ai làm gì)
e.g. The teacher made us do a lot of homework. (Giáo viên bắt chúng tôi làm rất nhiều bài tập ở nhà)
49. CN + be + so + tính từ + that + S + động từ. ( Đến mức mà )
CN + động từ + so + trạng từ
e.g.1. The exercise is so difficult that noone can do it. (Bài tập khó đến mức không ai làm được)
2. He spoke so quickly that I couldn’t understand him. (Anh ta nói nhanh đến mức mà tôi không thể hiểu được anh ta)
50. CN + be + such + ( tính từ ) + danh từ + that + CN + động từ.
e.g. It is such a difficult exercise that noone can do it. (Đó là một bài tập quá khó đến nỗi không ai có thể làm được)
51. It is ( very ) kind of smb to do smt ( Ai thật tốt bụng / tử tế khi làm gì)
e.g. It is very kind of you to help me. (Bạn thật tốt vì đã giúp tôi)
52. To find it + tính từ + to do smt
e.g. We find it difficult to learn English. (Chúng tôi thấy học tiếng Anh khó)
53. To make sure of smt ( Bảo đảm điều gì ) that + CN + động từ
e.g. 1. I have to make sure of that information. (Tôi phải bảo đảm chắc chắn về thông tin đó)
2. You have to make sure that you’ll pass the exam. (Bạn phải bảo đảm là bạn sẽ thi đỗ)
54. It takes ( smb ) + thời gian + to do smt ( Mất ( của ai ) bao nhiêu thời gian để làm gì)
e.g. It took me an hour to do this exercise. (Tôi mất một tiếng để làm bài này)
55. To spend + time / money + on smt ( Dành thời gian / tiền bạc vào cái gì)/doing smt làm gì
e.g. We spend a lot of time on TV/watching TV. (Chúng tôi dành nhiều thời gian xem TV)
56. To have no idea of smt = don’t know about smt ( Không biết về cái gì )
e.g. I have no idea of this word = I don’t know this word. (Tôi không biết từ này)
57. To advise smb to do smt ( Khuyên ai làm gì/not to do smt không làm gì )
e.g. Our teacher advises us to study hard. (Cô giáo khuyên chúng tôi học chăm chỉ)
58. To plan to do smt ( Dự định / có kế hoạch làm gì)
e.g. We planed to go for a picnic. (Chúng tôi dự định đi dã ngoại)
59. To invite smb to do smt (Mời ai làm gì)
e.g. They invited me to go to the cinema. (Họ mời tôi đi xem phim)
60. To offer smb smt (Mời / đề nghị ai cái gì)
e.g. He offered me a job in his company. (Anh ta mời tôi làm việc cho công ty anh ta)
61. To rely on smb (tin cậy, dựa dẫm vào ai)
e.g. You can rely on him. (Bạn có thể tin anh ấy)
62. To keep promise (Giữ lời hứa)
e.g. He always keeps promises. (Anh ấy luôn giữ lời hứa)
63. To be able to do smt = To be capable of + V_ing (Có khả năng làm gì)
e.g. I’m able to speak English = I am capable of speaking English. (Tôi có thể nói tiếng Anh)
64. To be good at ( + V_ing ) smt (Giỏi ( làm ) cái gì)
e.g. I’m good at ( playing ) tennis. (Tôi chơi quần vợt giỏi)
65. To prefer smt to smt ( Thích cái gì hơn cái gì ) /doing smt to doing smt: làm gì hơn làm gì
e.g. We prefer spending money than earning money. (Chúng tôi thích tiêu tiền hơn kiếm tiền)
66. To apologize for doing smt ( Xin lỗi ai vì đã làm gì )
e.g. I want to apologize for being rude to you. (Tôi muốn xin lỗi vì đã bất lịch sự với bạn)
67. Had ( ‘d ) better do smt ( Nên làm gì )/ not do smt ( Không nên làm gì )
e.g. 1. You’d better learn hard. (Bạn nên học chăm chỉ) 2. You’d better not go out. (Bạn không nên đi ra ngoài)
68. Would ( ‘d ) rather do smt (Thà làm gì )/ not do smt đừng làm gì
e.g. I’d rather stay at home. (Tôi thà ở nhà còn hơn)
69. Would ( ‘d ) rather smb did smt ( Muốn ai làm gì )
e.g. I’d rather you ( he / she ) stayed at home today. (Tôi muốn bạn / anh ấy / cô ấy ở nhà tối nay)
70. To suggest smb ( should ) do smt ( Gợi ý ai làm gì )
e.g. I suggested she ( should ) buy this house. (Tôi gợi ý cô ấy nên mua căn nhà này)
71. To suggest doing smt ( Gợi ý làm gì )
e.g. I suggested going for a walk. (Tôi gợi ý nên đi bộ)
72. Try to do ( Cố làm gì )
e.g. We tried to learn hard. (Chúng tôi đã cố học chăm chỉ)
73. Try doing smt ( Thử làm gì )
e.g. We tried cooking this food. (Chúng tôi đã thử nấu món ăn này)
74. To need to do smt( Cần làm gì )
e.g. You need to work harder. (Bạn cần làm việc tích cực hơn)
75. To need doing ( Cần được làm )
e.g. This car needs repairing. (Chiếc ôtô này cần được sửa)
76. To remember doing ( Nhớ đã làm gì )
e.g. I remember seeing this film. (Tôi nhớ là đã xem bộ phim này)
77. To remember to do ( Nhớ làm gì ) ( chưa làm cái này )
e.g. Remember to do your homework. (Hãy nhớ làm bài tập về nhà)
78. To have smt + PII ( Có cái gì được làm )
e.g. I’m going to have my house repainted. (Tôi sẽ sơn lại nhà người khác sơn, không phải mình sơn lấy)
= To have smb do smt ( Thuê ai làm gì ) Biology = I’m going to have my car repaired.
e.g. I’m going to have the garage repair my car. (Tôi thuê ga-ra để sửa xe)
79. To be busy doing smt ( Bận rộn làm gì )
e.g. We are busy preparing for our exam. (Chúng tôi đang bận rộn chuẩn bị cho kỳ thi)
80. To mind doing smt ( Phiền làm gì )
e.g. Do / Would you mind closing the door for me? (Bạn có thể đóng cửa giúp tôi không?)
81. To be used to doing smt ( Quen với việc làm gì )
e.g. We are used to getting up early. (Chúng tôi đã quen dậy sớm)
82. To stop to do smt ( Dừng lại để làm gì )
e.g. We stopped to buy some petrol. (Chúng tôi đã dừng lại để mua xăng)
83. To stop doing smt ( Thôi không làm gì nữa )
e.g. We stopped going out late. (Chúng tôi thôi không đi chơi khuya nữa)
84. Let smb do smt ( Để ai làm gì )
e.g. Let him come in. (Để anh ta vào)

By Mr. Duy"""[cite: 2]

# Hàm xử lý chuỗi ký tự xuống dòng để ghi gọn vào file text database
def ma_hoa_noi_dung(text):
    return text.replace("\n", "[NEWLINE]")

def gia_ma_noi_dung(text):
    return text.replace("[NEWLINE]", "\n")

# Tự động nạp dữ liệu gốc vào file sotay_data.txt nếu khởi chạy lần đầu
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        # Ghi File 1 vào danh mục Khác
        f.write(f"Khác|||Dữ liệu gốc File 1|||{ma_hoa_noi_dung(FILE_1_CONTENT)}\n")
        # Ghi File 2 vào danh mục Tiếng Anh
        f.write(f"Tiếng Anh|||84 Cấu trúc câu thông dụng (By Mr. Duy)|||{ma_hoa_noi_dung(FILE_2_CONTENT)}\n")

# Hàm đọc toàn bộ dữ liệu từ file
def doc_du_lieu():
    if not os.path.exists(DATA_FILE):
        return []
    danh_sach = []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if line_str:
                parts = line_str.split("|||")
                if len(parts) == 3:
                    loai, tieu_de, noi_dung_ma_hoa = parts
                    danh_sach.append({
                        "loai": loai,
                        "tieu_de": tieu_de,
                        "noi_dung": gia_ma_noi_dung(noi_dung_ma_hoa)
                    })
    return danh_sach

# Hàm thêm dữ liệu mới
def luu_du_lieu(loai, tieu_de, noi_dung):
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{loai}|||{tieu_de}|||{ma_hoa_noi_dung(noi_dung)}\n")

tat_ca_du_lieu = doc_du_lieu()

# --- PHẦN 1: GIAO DIỆN THÊM MỚI ---
st.header("➕ Thêm kiến thức mới")
mon_hoc = st.selectbox("Chọn mục muốn lưu:", ["Toán Học", "Tiếng Anh", "Khác"])
tieu_de = st.text_input("Tiêu đề ghi nhớ:")
noi_dung = st.text_area("Nội dung chi tiết:")

if st.button("Lưu lại vào hệ thống"):
    if tieu_de and noi_dung:
        luu_du_lieu(mon_hoc, tieu_de, noi_dung)
        st.success(f"🎉 Đã lưu thành công vào mục {mon_hoc}!")
        st.rerun()
    else:
        st.error("⚠️ Vui lòng nhập đầy đủ cả Tiêu đề và Nội dung!")

st.markdown("---")

# --- PHẦN 2: DANH SÁCH HIỂN THỊ ---
st.header("📖 Danh sách kiến thức đã lưu")
tab1, tab2, tab3 = st.tabs(["📐 Công thức Toán Học", "🔤 Từ vựng Tiếng Anh", "📁 Tài liệu khác (File đính kèm)"])

with tab1:
    co_du_lieu_toan = False
    for item in tat_ca_du_lieu:
        if item["loai"] == "Toán Học":
            co_du_lieu_toan = True
            with st.expander(f"📌 {item['tieu_de']}"):
                st.code(item["noi_dung"], language="markdown")
    if not co_du_lieu_toan:
        st.info("Chưa có công thức Toán nào được lưu.")

with tab2:
    co_du_lieu_anh = False
    for item in tat_ca_du_lieu:
        if item["loai"] == "Tiếng Anh":
            co_du_lieu_anh = True
            with st.expander(f"⭐ {item['tieu_de']}"):
                st.text(item["noi_dung"])
    if not co_du_lieu_anh:
        st.info("Chưa có dữ liệu Tiếng Anh nào được lưu.")

with tab3:
    co_du_lieu_khac = False
    for item in tat_ca_du_lieu:
        if item["loai"] == "Khác":
            co_du_lieu_khac = True
            with st.expander(f"📂 {item['tieu_de']}"):
                st.text(item["noi_dung"])
    if not co_du_lieu_khac:
        st.info("Chưa có tài liệu đính kèm nào khác.")
