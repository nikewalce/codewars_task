def int32_to_ip(int32):
    if int32 == 0:
        return "0.0.0.0"
    else:
        clean_bin = format(int32, '032b')  # 32-битная бинарная строка
        lst_oktet = [clean_bin[i:i+8] for i in range(0, 32, 8)]
        return ".".join(str(int(i, 2)) for i in lst_oktet)