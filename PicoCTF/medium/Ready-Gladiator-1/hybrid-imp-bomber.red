;redcode
;name Imp Ex
;assert 1
start:
    MOV 0, 1  
    SPL bomber 
    JMP start 

bomber:
    MOV bomb, bomb_offset  
    ADD #4, bomb_offset  
    JMP bomber          

bomb DAT #0            
bomb_offset EQU 10
end
