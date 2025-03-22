;redcode
;name Imp Ex
;assert 1
add #5, scan
mov bomb, @scan
jmp scan
bomb dat #0
scan equ 100
end
