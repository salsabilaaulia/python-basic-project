import turtle
import random
turtle.bgcolor("#008000")
turtle.title("Candi Warna-Warni")

# INPUT VARIABEL DAN VALIDASI INPUT
# Lapisan bata
lapisan_bawah = int(turtle.numinput("Input", "Jumlah batu bata pada lapisan paling bawah (input float akan dibulatkan ke bawah): ",
                minval = 1,
                maxval = 25))               

lapisan_atas =  int(turtle.numinput("Input", "Jumlah batu bata pada lapisan paling atas (input float akan dibulatkan ke bawah): ",
                minval = 1,
                maxval = lapisan_bawah))

# Ukuran bata
panjang_bata = int(turtle.numinput("Input", "Panjang satu buah bata (satuan berupa piksel dan input float akan dibulatkan ke bawah): ",
                minval = 1,
                maxval = 35))

lebar_bata = int(turtle.numinput("Input", "Lebar satu buah bata (satuan berupa piksel dan input float akan dibulatkan ke bawah): ",
                minval = 1,
                maxval = 25))

# IMPLEMENTASI INPUT DALAM TURTLE
# Pengaturan dan nilai awal
batu_bata = 0
start_point_x = panjang_bata*lapisan_bawah/2 - panjang_bata
start_point_y = 0 - (lebar_bata*(lapisan_bawah - lapisan_atas + 1)/2)
text_position_x = 0
text_position_y = start_point_y - 30
set_warna_bata = lapisan_bawah
start_point_bata = lapisan_bawah
turtle.pen(pencolor = "black", fillcolor = "#BC4A3C", speed = 0)

# Menggambar bata
while batu_bata < lapisan_bawah: 
    turtle.penup()
    turtle.setpos(start_point_x , start_point_y)
    turtle.begin_fill()
    turtle.pendown()  
    turtle.setheading(0)
    turtle.forward(panjang_bata)
    turtle.setheading(90)
    turtle.forward(lebar_bata)
    turtle.setheading(180)
    turtle.forward(panjang_bata)
    turtle.setheading(270)
    turtle.forward(lebar_bata)
    turtle.end_fill()
    start_point_x -= panjang_bata # menggeser posisi bata
    batu_bata += 1

    # membuat warna bata menjadi acak
    if lapisan_bawah < set_warna_bata and lapisan_bawah != lapisan_atas: # warna bata acak selain lapisan atas
            turtle.fillcolor(random.random(),random.random(),random.random())
            if batu_bata == lapisan_bawah - 1: # warna bata acak selain ujung terakhir
                    turtle.fillcolor("#BC4A3C")

    # tumpukan lapisan batu bata
    if batu_bata == lapisan_bawah:
        if batu_bata == lapisan_atas:
            turtle.hideturtle()  
            turtle.penup()
            break # agar lapisan bata berhenti sesuai lapisan atas
        else: # agar lapisan bata menjulang ke atas
            lapisan_bawah -= 1
            batu_bata = 0
            start_point_x = panjang_bata*lapisan_bawah/2 - panjang_bata
            start_point_y += lebar_bata
            if batu_bata == 0:
                turtle.fillcolor("#BC4A3C") # mengembalikan warna awal bata menjadi merah

# OUTPUT TOTAL BATU BATA
total_batu_bata = 0
for bata in range(start_point_bata, lapisan_atas - 1, -1):
   total_batu_bata += bata
turtle.setposition(text_position_x, text_position_y)
turtle.write(f"Candi warna-warni dengan {total_batu_bata} batu bata",
            align = "center",
            font = 30)

turtle.exitonclick()