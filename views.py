from django.shortcuts import render

def klvchen(req):
    print("ǰ������: ", req.POST)
    print("file:", req.FILES)

    for item in req.FILES:
        obj = req.FILES.get(item)      # ��ȡҪд����ļ�
        filename = obj.name            # ��ȡ�ļ���
        f = open(filename, 'wb')
        for line in obj.chunks():      # �ֿ�д��
            f.write(line)
        f.close()

    return render(req, "index.html")
