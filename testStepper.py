from Stepper

#stepper variables
#[stepPin, directionPin, enablePin]
testStepper = Stepper.stepper([22, 17, 23])

#test stepper
testStepper.step(3200, "right"); #steps, dir, speed, stayOn
