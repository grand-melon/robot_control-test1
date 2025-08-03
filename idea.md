#HW (Daban 6609)
MG Scale(1:100)
+Contraol Unit Mount Rack
+Battery Pack Rack

##구성도
1. 머리 (NeckServo, HeadLED) 
3. 왼팔 (L_ShoulderServo, L_ElbowServo)
4. 오른팔 (R_ShoulderServo, R_ElbowServo)
5. 왼손 (L_Hand)
6. 오른손 (R_Hand)
7. 허리 (WaistServo, CockpitServo)
9. 왼다리 (L_PelvisServo, L_KneeServo)
10. 오른다리 (R_PelvisServo, R_KneeServo)
11. 왼발 (L_Foot)
12. 오른발 (R_Foot)
13. 자세제어 (GyroModule)
14. 무장 (Laser1, Laser2)

##Pin MAP
1. Arduino Nano -1 (상체)
  D2 : NeckServo
  D3 : HeadLED
  D4 : L_ShoulderServo
  D5 : L_ElbowServo
  D6 : R_ShoulderServo
  D7 : R_ElbowServo
  D8 : L_Hand (Rotation)
  D9 : L_Hand (Motion)
  D10 : R_Hand (Rotation)
  D11 : R_Hand (Motion)
  D12 : WaistServo
  D13 : CockpitServo

2. Arduino Nano -2 (하체)
  D2 : L_PelvisServo
  D3 : L_KneeServo
  D4 : R_PelvisServo
  D5 : R_KneeServo
  D6 : L_Foot (Rotation)
  D7 : L_Foot (Motion)
  D8 : R_Foot (Rotation)
  D9 : R_Foot (Motion)
  D10 : GyroModule
  D11 : 
  D12 : 
  D13 : 


##테스트 범위
[1차]
머리, 왼팔, 오른팔, 왼다리, 오른다리

[2차]
왼손, 오른손, 왼발, 오른발, 허리
