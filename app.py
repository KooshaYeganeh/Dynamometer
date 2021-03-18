from flask import Flask , render_template , request, url_for
import math

app = Flask(__name__)




@app.route("/")
def menu():
    return render_template("menu.html")




@app.route("/aerodynamic")
def aero():
    return render_template("aerodynamic.html")

@app.route("/aerodynamic" , methods = ["POST"])
def aerodynamic_force():
    height = request.form["Height"]
    width = request.form["Width"]
    dragco = request.form["Drag Coefficient"]
    speed = request.form["Speed"]
    
    Frontal_area = 0.8 * float(height) * float(width)
    drag_force = 0.048 * float(dragco) * float(Frontal_area) * (float(speed)**2)
    return render_template("aerodynamic.html", drag = drag_force)




@app.route("/clutch")
def clutch():
    return render_template("clutch.html")

@app.route("/clutch" , methods = ["POST"])
def clutch_calculation():
    inner_friction = request.form["innerfriction"]
    outer_friction = request.form["outerfriction"]
    number_friction = request.form["number"]
    pressure_force = request.form["pressure"]
    coefficient = request.form["coefficient"]
    
    
    i = float(inner_friction)
    o = float(outer_friction)
    n = int(number_friction)
    p = float(pressure_force)
    co = float(coefficient)
    
    clutch1 = (2/3) * ((((o**3)-(i**3)))/((o**2) - (i**2)))
    clutch2 = p * float(clutch1) * co * n
    return render_template("/clutch.html" , clutch1 = clutch1 , clutch2 = clutch2)




@app.route("/center_of_gravity")
def center_of_gravity1():
    return render_template("center_of_gravity.html")


@app.route("/center_of_gravity" , methods = ["POST"])

def center():
    wheelbase = request.form["wheelbase"]
    frontmass = request.form["frontmass"]
    rearmass = request.form["rearmass"]
    gravity = request.form["gravity"]
    
    g = float(gravity)
    W = float(wheelbase)
    f = float(frontmass) * g
    r = float(rearmass) * g
    
    
    total = (f + r)
    
    C = (W * f)/total
    B = W - C

    return render_template("center_of_gravity.html" , cgravity = C , bgravity = B )
    
    


@app.route("/gradeability")
def grade():
    return render_template("gradeability.html")

@app.route("/gradeability" , methods = ["POST"])
def gradeability_calculation():
    first_gear = request.form["first"]
    seccond_gear = request.form["seccond"]
    third_gear = request.form["third"]
    resistance = request.form["resistance"]
    mass = request.form["mass"]
    
    

    a = (100*((float(first_gear)/((float(mass)*9.81))- float(resistance))))
    b = (100*((float(seccond_gear)/((float(mass)*9.81))- float(resistance))))
    c = (100*((float(third_gear)/((float(mass)*9.81))- float(resistance))))
    
    
    mylist = (a , b , c)
    return render_template("gradeability.html" , mylist = mylist)
    
            
    
@app.route("/maximum_speed_of_road_curve")
def maximum_speed_of_road_curve():
    return render_template("maximum_speed_of_road_curve.html")


@app.route("/maximum_speed_of_road_curve" , methods = ["POST"])

def max():
    radius = request.form["radius"]
    gravity = request.form["gravity"]
    coefficient = request.form["coefficient"]
    angle = request.form["angle"]
    
    r = float(radius)
    g = float(gravity)
    c = float(coefficient)
    a = float(angle)
    sinangle = math.sin(math.radians(a))
    cosangle = math.cos(math.radians(a))
    
    speed1 = math.sqrt((r*g)*((sinangle+(c*(cosangle)))/(cosangle-(c*(sinangle)))))
    speed2 = (18/5)*speed1
    
    
    return render_template("maximum_speed_of_road_curve.html" , speed = speed2)
    



    
    
@app.route("/5_speed_transmission")
def fivespeed():
    return render_template("5_speed_transmission.html")

 
@app.route("/5_speed_transmission" , methods = ["POST"])
def five_speed_transmission():
    first_rev = request.form["first rev"]
    second_rev = request.form["second rev"]
    first_gear = request.form["first gear"]
    second_gear = request.form["second gear"]
    third_gear = request.form["third gear"]
    forth_gear = request.form["forth gear"]
    fifth_gear = request.form["fifth gear"]
    
    First_rev  = int(first_rev)
    Second_rev = int(second_rev)
    First_gear = float(first_gear)
    Second_gear =float(second_gear)
    Third_gear = float(third_gear)
    Forth_gear = float(forth_gear)
    Fifth_gear = float(fifth_gear)
    
    
            
            
            
             
            
    ratio = (First_gear,Second_gear,Third_gear,Forth_gear,Fifth_gear)
    new = []
    for rev in range(First_rev , Second_rev):
        for gear in ratio:
            result = (rev/gear)
            new.append(result)
    return render_template("5_speed_transmission.html" , result1 = new)            
                
       
     
                            
    


  
@app.route("/6_speed_transmission")
def sixspeed():
    return render_template("6_speed_transmission.html")

@app.route("/6_speed_transmission" , methods = ["POST"])
def six_speed_out_cal():
        first_rev = request.form["first rev"]
        second_rev = request.form["second rev"]
        first_gear = request.form["one gear"]
        second_gear = request.form["two gear"]
        third_gear = request.form["three gear"]
        forth_gear = request.form["four gear"]
        fifth_gear = request.form["five gear"]
        six_gear =  request.form["six gear"]
        
        
        First_rev  = int(first_rev)
        Second_rev = int(second_rev)
        First_gear = float(first_gear)
        Second_gear =float(second_gear)
        Third_gear = float(third_gear)
        Forth_gear = float(forth_gear)
        Fifth_gear = float(fifth_gear)
        Six_gear = float(six_gear)   
    
            
            
            
             
            
        ratio = (First_gear,Second_gear,Third_gear,Forth_gear,Fifth_gear,Six_gear)
        new = []
        for rev in range(First_rev , Second_rev):
            for gear in ratio:
                result = (rev/gear)
                new.append(result)
        return render_template("6_speed_transmission.html" , result1 = new) 



@app.route("/7_speed_transmission")
def sevenspeed():
    return render_template("7_speed_transmission.html")

@app.route("/7_speed_transmission" , methods = ["POST"])
def seven_speed_cal():
        first_rev = request.form["first rev"]
        second_rev = request.form["second rev"]
        first_gear = request.form["one gear"]
        second_gear = request.form["two gear"]
        third_gear = request.form["three gear"]
        forth_gear = request.form["four gear"]
        fifth_gear = request.form["five gear"]
        six_gear =  request.form["six gear"]
        seven_gear = request.form["seven gear"]
        
        
        First_rev  = int(first_rev)
        Second_rev = int(second_rev)
        First_gear = float(first_gear)
        Second_gear =float(second_gear)
        Third_gear = float(third_gear)
        Forth_gear = float(forth_gear)
        Fifth_gear = float(fifth_gear)
        Six_gear = float(six_gear)
        Seven_gear = float(seven_gear)
    
            
            
            
             
            
        ratio = (First_gear,Second_gear,Third_gear,Forth_gear,Fifth_gear,Six_gear,Seven_gear)
        new = []
        for rev in range(First_rev , Second_rev):
            for gear in ratio:
                result = (rev/gear)
                new.append(result)
                
        return render_template("7_speed_transmission.html" , result1 = new) 



@app.route("/8_speed_transmission")
def eightspeed():
    return render_template("8_speed_transmission.html")

@app.route("/8_speed_transmission" , methods = ["POST"])
def eight_speed_cal():
        first_rev = request.form["first rev"]
        second_rev = request.form["second rev"]
        first_gear = request.form["one gear"]
        second_gear = request.form["two gear"]
        third_gear = request.form["three gear"]
        forth_gear = request.form["four gear"]
        fifth_gear = request.form["five gear"]
        six_gear =  request.form["six gear"]
        seven_gear = request.form["seven gear"]
        eight_gear = request.form["eight gear"]
        
        First_rev  = int(first_rev)
        Second_rev = int(second_rev)
        First_gear = float(first_gear)
        Second_gear=float(second_gear)
        Third_gear = float(third_gear)
        Forth_gear = float(forth_gear)
        Fifth_gear = float(fifth_gear)
        Six_gear   = float(six_gear)
        Seven_gear = float(seven_gear)
        Eight_gear = float(eight_gear)
    
            
            
            
             
            
        ratio = (First_gear,Second_gear,Third_gear,Forth_gear,Fifth_gear,Six_gear,Seven_gear,Eight_gear)
        new = []
        for rev in range(First_rev , Second_rev):
            for gear in ratio:
                result = (rev/gear)
                new.append(result)
                
        return render_template("8_speed_transmission.html" , result1 = new) 



@app.route("/9_speed_transmission")
def ninespeed():
    return render_template("9_speed_transmission.html")

@app.route("/9_speed_transmission" , methods = ["POST"])
def nine_speed_transmission():
    
    
        first_rev = request.form["first rev"]
        second_rev = request.form["second rev"]
        first_gear = request.form["one gear"]
        second_gear = request.form["two gear"]
        third_gear = request.form["three gear"]
        forth_gear = request.form["four gear"]
        fifth_gear = request.form["five gear"]
        six_gear =  request.form["six gear"]
        seven_gear = request.form["seven gear"]
        eight_gear = request.form["eight gear"]
        nine_gear = request.form["nine gear"]
        
        First_rev  = int(first_rev)
        Second_rev = int(second_rev)
        First_gear = float(first_gear)
        Second_gear=float(second_gear)
        Third_gear = float(third_gear)
        Forth_gear = float(forth_gear)
        Fifth_gear = float(fifth_gear)
        Six_gear   = float(six_gear)
        Seven_gear = float(seven_gear)
        Eight_gear = float(eight_gear)
        Nine_gear = float (nine_gear)
    
            
            
            
             
            
        ratio = (First_gear,Second_gear,Third_gear,Forth_gear,Fifth_gear,Six_gear,Seven_gear,Eight_gear,Nine_gear)
        new = []
        for rev in range(First_rev , Second_rev):
            for gear in ratio:
                result = (rev/gear)
                new.append(result)
                
        return render_template("9_speed_transmission.html" , result1 = new) 
    







@app.route("/Calculation_of_Output_rev")
def out_rev_diff():
    return render_template("Calculation_of_Output_rev.html")

@app.route("/Calculation_of_Output_rev" , methods=["POST"])
def out_rev_Diff_cal():
    rev_gear_ratio = request.form["rev gear ratio"]
    input_rev  = request.form["input rev"]
    
    r = float(rev_gear_ratio)
    i = float(input_rev)
    
    output_rev = i/r
    
    return render_template("Calculation_of_Output_rev.html" , output_rev = output_rev)   






@app.route("/Gear_ratio_Calculation_of_Differential_Gear_Diameter")
def diff_Gear_ratio():
    return render_template("Gear_ratio_Calculation_of_Differential_Gear_Diameter.html")

@app.route("/Gear_ratio_Calculation_of_Differential_Gear_Diameter", methods=["POST"])
def diff_Gear_ratio_cal():
    input_diameter = request.form["input diameter"]
    output_diameter = request.form["output diameter"]
    
    i = float(input_diameter)
    o = float(output_diameter)

    gearratio = float(o/i)
    return render_template("Gear_ratio_Calculation_of_Differential_Gear_Diameter.html" , gear_ratio = gearratio)



@app.route("/Calculation_of_Output_torque")
def out_torque():
    return render_template("Calculation_of_Output_torque.html")


@app.route("/Calculation_of_Output_torque" , methods=["POST"])
def out_torque_cal():
    input_torque  = request.form["input torque"]
    gear_ratio  = request.form["gear ratio"]
    
    i = float(input_torque)
    g = float(gear_ratio)
    out_torque = float(g * i)
    return render_template("Calculation_of_Output_torque.html" , output_torque = out_torque)


@app.route("/Gear_ratio_Calculation_of_Differential_Number_of_teeth")
def teeth():
    return render_template("Gear_ratio_Calculation_of_Differential_Number_of_teeth.html")


@app.route("/Gear_ratio_Calculation_of_Differential_Number_of_teeth" , methods = ["POST"])
def teeth_cal():
    Output_Gear_Teeth_Number = request.form["Output Gear Teeth Number"]
    Input_Gear_Teeth_Number = request.form["Input Gear Teeth Number"]
    
    o = int(Output_Gear_Teeth_Number)
    i = int(Input_Gear_Teeth_Number)
    
    gear_ratio = float(o/i)
    
    return render_template("Gear_ratio_Calculation_of_Differential_Number_of_teeth.html" , Gear_ratio = gear_ratio )




@app.route("/Gear_ratio_Calculation_of_Differential_input_and_output_rev")
def gear_ratio_rev():
    return render_template("Gear_ratio_Calculation_of_Differential_input_and_output_rev.html")

@app.route("/Gear_ratio_Calculation_of_Differential_input_and_output_rev" , methods = ["POST"])
def gear_ratio_rev_cal():
    Input_rev = request.form["Input rev"]
    Output_rev = request.form["Output rev"]
    
    i = int(Input_rev)
    o = int(Output_rev)
    
    gear = float(i/o)

    return render_template("Gear_ratio_Calculation_of_Differential_input_and_output_rev.html" ,Gear_ratio = gear )




@app.route("/wheel_rev_output")
def wheel_torque_output():
    return render_template("wheel_torque_and_rev_output.html")
# @app.route("/wheel_rev_output" , methods=["POST"])
# def Weel_torque():
    


@app.route("/calculation_of_tractive_force_5speed")
def five_traction():
     return render_template("calculation_of_tractive_force_5speed.html")
 
@app.route("/calculation_of_tractive_force_5speed" , methods=["POST"])
def traction_five_cal():

        first_gear = request.form["one gear"]
        second_gear = request.form["two gear"]
        third_gear = request.form["three gear"]
        forth_gear = request.form["four gear"]
        fifth_gear = request.form["five gear"]
        first_torque = request.form["first torque"]
        second_torque = request.form["second torque"]
        wheel_radius = request.form["wheel radius"]
        diff_ratio = request.form["diff ratio"]
        
        First_gear = float(first_gear)
        Second_gear=float(second_gear)
        Third_gear = float(third_gear)
        Forth_gear = float(forth_gear)
        Fifth_gear = float(fifth_gear)
        First_torque = int(first_torque)
        Second_torque = int(second_torque)
        Wheel_radius = float(wheel_radius)
        Diff_ratio = float(diff_ratio)   
            
            
            
             
            
        ratio = (First_gear,Second_gear,Third_gear,Forth_gear,Fifth_gear)
        new = []
        for torque in range(First_torque , Second_torque):
            for gear in ratio:
                T_trans = (torque*(float(gear)))
                T_diff = (T_trans * Diff_ratio)
                result = (T_diff/Wheel_radius)
                new.append(result)
                
        return render_template("calculation_of_tractive_force_5speed.html" , result1 = new) 
    
 
 
 
 
 
@app.route("/calculation_of_tractive_force_6speed")
def six_traction():
    return render_template("/calculation_of_tractive_force_6speed.html")



@app.route("/calculation_of_tractive_force_6speed" , methods=["POST"])
def six_speed_traction():
        first_gear = request.form["one gear"]
        second_gear = request.form["two gear"]
        third_gear = request.form["three gear"]
        forth_gear = request.form["four gear"]
        fifth_gear = request.form["five gear"]
        six_gear =  request.form["six gear"]
        first_torque = request.form["first torque"]
        second_torque = request.form["second torque"]
        wheel_radius = request.form["wheel radius"]
        diff_ratio = request.form["diff ratio"]
        
        First_gear = float(first_gear)
        Second_gear=float(second_gear)
        Third_gear = float(third_gear)
        Forth_gear = float(forth_gear)
        Fifth_gear = float(fifth_gear)
        Six_gear = float(six_gear)
        First_torque = int(first_torque)
        Second_torque = int(second_torque)
        Wheel_radius = float(wheel_radius)
        Diff_ratio = float(diff_ratio)   
            
            
            
             
            
        ratio = (First_gear,Second_gear,Third_gear,Forth_gear,Fifth_gear,Six_gear)
        new = []
        for torque in range(First_torque , Second_torque):
            for gear in ratio:
                T_trans = (torque*(float(gear)))
                T_diff = (T_trans * Diff_ratio)
                result = (T_diff/Wheel_radius)
                new.append(result)
                
        return render_template("calculation_of_tractive_force_6speed.html" , result1 = new) 







@app.route("/calculation_of_tractive_force_7speed")
def seven_speed():
    return render_template("calculation_of_tractive_force_7speed.html")


@app.route("/calculation_of_tractive_force_7speed" , methods=["POST"])
def seven_speed_traction():
        first_gear = request.form["one gear"]
        second_gear = request.form["two gear"]
        third_gear = request.form["three gear"]
        forth_gear = request.form["four gear"]
        fifth_gear = request.form["five gear"]
        six_gear =  request.form["six gear"]
        seven_gear =  request.form["seven gear"]
        first_torque = request.form["first torque"]
        second_torque = request.form["second torque"]
        wheel_radius = request.form["wheel radius"]
        diff_ratio = request.form["diff ratio"]
        
        First_gear = float(first_gear)
        Second_gear=float(second_gear)
        Third_gear = float(third_gear)
        Forth_gear = float(forth_gear)
        Fifth_gear = float(fifth_gear)
        Six_gear = float(six_gear)
        Seven_gear  = float(seven_gear)
        First_torque = int(first_torque)
        Second_torque = int(second_torque)
        Wheel_radius = float(wheel_radius)
        Diff_ratio = float(diff_ratio)   
            
            
            
             
            
        ratio = (First_gear,Second_gear,Third_gear,Forth_gear,Fifth_gear,Six_gear,Seven_gear)
        new = []
        for torque in range(First_torque , Second_torque):
            for gear in ratio:
                T_trans = (torque*(float(gear)))
                T_diff = (T_trans * Diff_ratio)
                result = (T_diff/Wheel_radius)
                new.append(result)
                
        return render_template("calculation_of_tractive_force_7speed.html" , result1 = new) 



@app.route("/calculation_of_tractive_force_8speed")
def eight_speed():
    return render_template("calculation_of_tractive_force_8speed.html")


@app.route("/calculation_of_tractive_force_8speed" , methods = ["POST"])
def eight_speed_traction_cal():
    
    first_gear = request.form["one gear"]
    second_gear = request.form["two gear"]
    third_gear = request.form["three gear"]
    forth_gear = request.form["four gear"]
    fifth_gear = request.form["five gear"]
    six_gear =  request.form["six gear"]
    seven_gear =  request.form["seven gear"]
    eight_gear = request.form["eight gear"]
    
    first_torque = request.form["first torque"]
    second_torque = request.form["second torque"]
    wheel_radius = request.form["wheel radius"]
    diff_ratio = request.form["diff ratio"]
    
    First_gear = float(first_gear)
    Second_gear=float(second_gear)
    Third_gear = float(third_gear)
    Forth_gear = float(forth_gear)
    Fifth_gear = float(fifth_gear)
    Six_gear = float(six_gear)
    Seven_gear  = float(seven_gear)
    Eight_gear = float(eight_gear)
    First_torque = int(first_torque)
    Second_torque = int(second_torque)
    Wheel_radius = float(wheel_radius)
    Diff_ratio = float(diff_ratio)   
        
        
        
            
        
    ratio = (First_gear,Second_gear,Third_gear,Forth_gear,Fifth_gear,Six_gear,Seven_gear,Eight_gear)
    new = []
    for torque in range(First_torque , Second_torque):
        for gear in ratio:
            T_trans = (torque*(float(gear)))
            T_diff = (T_trans * Diff_ratio)
            result = (T_diff/Wheel_radius)
            new.append(result)
            
    return render_template("calculation_of_tractive_force_8speed.html" , result1 = new) 


@app.route("/calculation_of_tractive_force_9speed")
def nine_speed():
    return render_template("calculation_of_tractive_force_9speed.html")

@app.route("//calculation_of_tractive_force_9speed" , methods = ["POST"])
def nine_speed_traction_cal():
    
    first_gear = request.form["one gear"]
    second_gear = request.form["two gear"]
    third_gear = request.form["three gear"]
    forth_gear = request.form["four gear"]
    fifth_gear = request.form["five gear"]
    six_gear =  request.form["six gear"]
    seven_gear =  request.form["seven gear"]
    eight_gear = request.form["eigth gear"]
    nine_gear = request.form["nine gear"]
    
    first_torque = request.form["first torque"]
    second_torque = request.form["second torque"]
    wheel_radius = request.form["wheel radius"]
    diff_ratio = request.form["diff ratio"]
    
    First_gear = float(first_gear)
    Second_gear=float(second_gear)
    Third_gear = float(third_gear)
    Forth_gear = float(forth_gear)
    Fifth_gear = float(fifth_gear)
    Six_gear = float(six_gear)
    Seven_gear  = float(seven_gear)
    Eight_gear = float(eight_gear)
    Nine_gear  = float(nine_gear)
    First_torque = int(first_torque)
    Second_torque = int(second_torque)
    Wheel_radius = float(wheel_radius)
    Diff_ratio = float(diff_ratio)   
        
        
        
            
        
    ratio = (First_gear,Second_gear,Third_gear,Forth_gear,Fifth_gear,Six_gear,Seven_gear,Eight_gear,Nine_gear)
    new = []
    for torque in range(First_torque , Second_torque):
        for gear in ratio:
            T_trans = (torque*(float(gear)))
            T_diff = (T_trans * Diff_ratio)
            result = (T_diff/Wheel_radius)
            new.append(result)
            
    return render_template("calculation_of_tractive_force_9speed.html" , result1 = new) 



@app.route("/weight_transfer_of_turning")
def weight_transfer_of_turning():
    return render_template("weight_transfer_of_turning.html")



@app.route("/lateral_sliding_acceleration")
def lateral_sliding_acceleration():
    return render_template("lateral_sliding_acceleration.html")



@app.route("/rollover_speed")
def rollover():
    return render_template("rollover_speed.html")

@app.route("/rollover_speed" , methods = ["POST"])
def rollover_speed_cal():
    
    
    road_radius = request.form["road radius"]
    center_gravity = request.form["center gravity"]
    track = request.form["track"]
    angle = request.form["angle"]
    lateral_sliding = request.form["lateral sliding"]
    
    Road_radius = float(road_radius)
    center_of_gravity = float(center_gravity)
    Track = float(track)
    Angle = float(angle)
    Lateral_Sliding = float(lateral_sliding)
    
    part_one = (center_of_gravity)*(math.sin(math.radians(Angle)))
    part_two = (Track/2)*(math.cos(math.radians(Angle)))
    part_three = (Road_radius)*(Lateral_Sliding)*(center_of_gravity)
    part_four = (center_of_gravity)*(math.cos(math.radians(Angle)))
    part_five = (Track/2)*(math.sin(math.radians(Angle)))
    part_six = (Road_radius) * 9.8
    rollover = math.sqrt((part_six*((part_one)+(part_two))+(part_three))/((part_four)-(part_five)))
    rolloverspeed = rollover  * 3.6
     
    return render_template("rollover_speed.html", one1=rolloverspeed)






@app.route("/brake_Time_to_Stop")
def time_to_stop():
    return render_template("brake_Time_to_Stop.html")

@app.route("/brake_Time_to_Stop", methods = ["POST"])
def time_stop():
    speed = request.form["Speed"]
    acceleration =request.form["acceleration"]
    reaction_Driver = request.form["Reaction Time of Driver"]
    
    Speed = int(speed)
    Acceleration = float(acceleration)
    Reaction_Driver = float(reaction_Driver)

    result = Reaction_Driver + (Speed/Acceleration)
    return render_template("brake_Time_to_Stop.html" , result = result)


@app.route("/power_of_brake")
def power_of_brake():
    return render_template("Power_of_Brake.html")

@app.route("/power_of_brake", methods = ["POST"])
def power_of_braking():
    braking_time = request.form["braking time"]
    braking_work = request.form["Braking work"]
    
    Braking_time = float(braking_time)
    Braking_work = float(braking_work)
    
    power_brake = Braking_work/Braking_time
    return render_template("Power_of_Brake.html" , power = power_brake)




@app.route("/Work_of_Brake")
def work_of_brake():
    return render_template("Work_of_Brake.html")

@app.route("/Work_of_Brake", methods = ["POST"])
def work():
    braking_force = request.form["braking force"]
    diameter = request.form["diameter"]
    rotation = request.form["rotation"]
    
    Braking_force = float(braking_force)
    Diameter = float(diameter)
    Rotation = int(rotation)
    
    working = Braking_force * (3.14 * Diameter) * Rotation
    return render_template("Work_of_Brake.html" , work = working)    



@app.route("/Brake_Distance_Length")
def brake():
    return render_template("Brake_Distance_Length.html")

@app.route("/Brake_Distance_Length" , methods = ["POST"])
def brake_distance():
    
    speed = request.form["Speed"]
    acceleration = request.form["acceleration"]
    
    Speed = float(speed)
    Acceleration=float(acceleration)
    
    brake_distance = (Speed**2)/(2*Acceleration)
    
    return render_template("Brake_Distance_Length.html" , brake_distance = brake_distance)
    
    
    

    
@app.route("/vehicle_speed_with_5_speed_transmission")
def Calculation_five_vehicle_speed():
    return render_template("vehicle_speed_with_5_speed_transmission.html")


@app.route("/vehicle_speed_with_5_speed_transmission" , methods=["POST"])
def vehicle_5_speed():
    
    
    first_rev = request.form["first rev"]
    second_rev = request.form["second rev"]
    one_gear = request.form["one gear"]
    two_gear = request.form["two gear"]
    three_gear = request.form["three gear"]
    four_gear = request.form["four gear"]
    five_gear = request.form["five gear"]
    differental = request.form["Differential ratio"]
    tyre_radius = request.form["Radius"]
    
    
    First_rev = int(first_rev)
    Second_rev = int(second_rev)
    One_gear = float(one_gear)
    Two_gear  = float(two_gear)
    Three_gear = float(three_gear)
    Four_gear = float(four_gear)
    Five_gear = float(five_gear)
    Differental = float(differental)
    Tyre_radius = float(tyre_radius)
    
    
    gears = (One_gear,Two_gear,Three_gear,Four_gear,Five_gear)
    new = []
    for rev in range(First_rev , Second_rev):
        for gear in gears:
            transmission_output = (rev/gear)
            differental_output = transmission_output * Differental
            translation = (float(differental_output)/60)
            speed = (2*3.14*Tyre_radius) * translation
            new.append(speed)
            
    return render_template("vehicle_speed_with_5_speed_transmission.html", speed = new)    

@app.route("/vehicle_speed_with_6_speed_transmission")
def Calculation_six_vehicle_speed():
    return render_template("vehicle_speed_with_6_speed_transmission.html")



@app.route("/vehicle_speed_with_6_speed_transmission" , methods = ["POST"])
def vehicle_6_speed():
    
    
    first_rev = request.form["first rev"]
    second_rev = request.form["second rev"]
    one_gear = request.form["one gear"]
    two_gear = request.form["two gear"]
    three_gear = request.form["three gear"]
    four_gear = request.form["four gear"]
    five_gear = request.form["five gear"]
    six_gear = request.form["six gear"]
    differental = request.form["Differential ratio"]
    tyre_radius = request.form["Radius"]
    
    
    First_rev = int(first_rev)
    Second_rev = int(second_rev)
    One_gear = float(one_gear)
    Two_gear  = float(two_gear)
    Three_gear = float(three_gear)
    Four_gear = float(four_gear)
    Five_gear = float(five_gear)
    Six_gear = float(six_gear)
    Differental = float(differental)
    Tyre_radius = float(tyre_radius)
    
    
    gears = (One_gear,Two_gear,Three_gear,Four_gear,Five_gear,Six_gear)
    new = []
    for rev in range(First_rev , Second_rev):
        for gear in gears:
            transmission_output = (rev/gear)
            differental_output = transmission_output * Differental
            translation = (float(differental_output)/60)
            speed = (2*3.14*Tyre_radius) * translation
            new.append(speed)
            
    return render_template("vehicle_speed_with_6_speed_transmission.html", speed = new)  




@app.route("/vehicle_speed_with_7_speed_transmission")
def Calculation_seven_vehicle_speed():
    return render_template("vehicle_speed_with_7_speed_transmission.html")

@app.route("/vehicle_speed_with_7_speed_transmission" , methods = ["POST"])
def seven_vehicle_speed():
    first_rev = request.form["first rev"]
    second_rev = request.form["second rev"]
    one_gear = request.form["one gear"]
    two_gear = request.form["two gear"]
    three_gear = request.form["three gear"]
    four_gear = request.form["four gear"]
    five_gear = request.form["five gear"]
    six_gear = request.form["six gear"]
    seven_gear = request.form["seven gear"]
    differental = request.form["Differential ratio"]
    tyre_radius = request.form["Radius"]
    
    
    First_rev = int(first_rev)
    Second_rev = int(second_rev)
    One_gear = float(one_gear)
    Two_gear  = float(two_gear)
    Three_gear = float(three_gear)
    Four_gear = float(four_gear)
    Five_gear = float(five_gear)
    Six_gear = float(six_gear)
    Seven_gear = float(seven_gear)
    Differental = float(differental)
    Tyre_radius = float(tyre_radius)
    
    
    gears = (One_gear,Two_gear,Three_gear,Four_gear,Five_gear,Six_gear,Seven_gear)
    new = []
    for rev in range(First_rev , Second_rev):
        for gear in gears:
            transmission_output = (rev/gear)
            differental_output = transmission_output * Differental
            translation = (float(differental_output)/60)
            speed = (2*3.14*Tyre_radius) * translation
            new.append(speed)
            
    return render_template("vehicle_speed_with_7_speed_transmission.html", speed = new)
    




@app.route("/vehicle_speed_with_8_speed_transmission")
def Calculation_eight_vehicle_speed():
    return render_template("vehicle_speed_with_8_speed_transmission.html")


@app.route("/vehicle_speed_with_8_speed_transmission" , methods = ["POST"])
def eight_vehicle_speed():
    first_rev = request.form["first rev"]
    second_rev = request.form["second rev"]
    one_gear = request.form["one gear"]
    two_gear = request.form["two gear"]
    three_gear = request.form["three gear"]
    four_gear = request.form["four gear"]
    five_gear = request.form["five gear"]
    six_gear = request.form["six gear"]
    seven_gear = request.form["seven gear"]
    eight_gear = request.form["eight gear"]
    differental = request.form["Differential ratio"]
    tyre_radius = request.form["Radius"]
    
    
    First_rev = int(first_rev)
    Second_rev = int(second_rev)
    One_gear = float(one_gear)
    Two_gear  = float(two_gear)
    Three_gear = float(three_gear)
    Four_gear = float(four_gear)
    Five_gear = float(five_gear)
    Six_gear = float(six_gear)
    Seven_gear = float(seven_gear)
    Eight_gear = float(eight_gear)
    Differental = float(differental)
    Tyre_radius = float(tyre_radius)
    
    
    gears = (One_gear,Two_gear,Three_gear,Four_gear,Five_gear,Six_gear,Seven_gear,Eight_gear)
    new = []
    for rev in range(First_rev , Second_rev):
        for gear in gears:
            transmission_output = (rev/gear)
            differental_output = transmission_output * Differental
            translation = (float(differental_output)/60)
            speed = (2*3.14*Tyre_radius) * translation
            new.append(speed)
            
    return render_template("vehicle_speed_with_8_speed_transmission.html", speed = new)




@app.route("/vehicle_speed_with_9_speed_transmission")
def Calculation_nine_vehicle_speed():
    return render_template("vehicle_speed_with_9_speed_transmission.html")




@app.route("/vehicle_speed_with_9_speed_transmission" , methods = ["POST"])
def nine_vehicle_speed():
    first_rev = request.form["first rev"]
    second_rev = request.form["second rev"]
    one_gear = request.form["one gear"]
    two_gear = request.form["two gear"]
    three_gear = request.form["three gear"]
    four_gear = request.form["four gear"]
    five_gear = request.form["five gear"]
    six_gear = request.form["six gear"]
    seven_gear = request.form["seven gear"]
    eight_gear = request.form["eight gear"]
    nine_gear = request.form["nine gear"]
    differental = request.form["Differential ratio"]
    tyre_radius = request.form["Radius"]
    
    
    First_rev = int(first_rev)
    Second_rev = int(second_rev)
    One_gear = float(one_gear)
    Two_gear  = float(two_gear)
    Three_gear = float(three_gear)
    Four_gear = float(four_gear)
    Five_gear = float(five_gear)
    Six_gear = float(six_gear)
    Seven_gear = float(seven_gear)
    Eight_gear = float(eight_gear)
    Nine_gear = float(nine_gear)
    Differental = float(differental)
    Tyre_radius = float(tyre_radius)
    
    
    gears = (One_gear,Two_gear,Three_gear,Four_gear,Five_gear,Six_gear,Seven_gear,Eight_gear,Nine_gear)
    new = []
    for rev in range(First_rev , Second_rev):
        for gear in gears:
            transmission_output = (rev/gear)
            differental_output = transmission_output * Differental
            translation = (float(differental_output)/60)
            speed = (2*3.14*Tyre_radius) * translation
            new.append(speed)
            
    return render_template("vehicle_speed_with_9_speed_transmission.html", speed = new)





@app.route("/refreancetable")
def ref():
    return render_template("refreancetable.html")


app.run(debug=True)