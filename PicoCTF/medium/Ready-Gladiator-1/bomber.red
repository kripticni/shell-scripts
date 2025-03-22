;redcode
;assert 1

start:
    spl bomber
    spl bomber
    spl bomber
    jmp start

bomber:
    mov bomb, @ptr  
    add #7, ptr  
    jmp bomber 

bomb:
    dat #0

ptr:
    dat #100

end
