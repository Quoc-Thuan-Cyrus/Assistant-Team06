def test_new_offices_lookup():
    # Kiểm tra tra cứu phòng Đào tạo (Training Office)
    assert "F.01" in reply("where is training")
    # Kiểm tra tra cứu phòng Công tác Sinh viên (Student Affairs)
    assert "A.01" in reply("where is student affairs")