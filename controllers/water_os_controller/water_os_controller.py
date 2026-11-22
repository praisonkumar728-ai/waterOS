from controller import Supervisor
import math
import time

robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

# Animated water parcels travel through the treatment line.
particles = []
for i in range(18):
    node = robot.getFromDef("FLOW_%02d" % i)
    if node:
        particles.append(node.getField("translation"))

pump = robot.getFromDef("PUMP_BODY")
valve = robot.getFromDef("VALVE")
pump_rotation = pump.getField("rotation") if pump else None
valve_translation = valve.getField("translation") if valve else None

# Three demonstration scenarios. Values are illustrative simulated inputs,
# not calibrated measurements or water-safety certification.
scenarios = [
    {
        "name": "SCENARIO 1 - Heavy rainfall runoff",
        "ph": 6.8, "turbidity": 82, "tds": 420, "salinity": 0.4,
        "route": "INTENSIVE FILTRATION", "pump": True, "bypass": False
    },
    {
        "name": "SCENARIO 2 - Saline intrusion",
        "ph": 7.4, "turbidity": 28, "tds": 1450, "salinity": 2.8,
        "route": "HOLD / SPECIALIZED TREATMENT", "pump": False, "bypass": True
    },
    {
        "name": "SCENARIO 3 - Moderate runoff",
        "ph": 7.1, "turbidity": 18, "tds": 360, "salinity": 0.3,
        "route": "STANDARD FILTRATION", "pump": True, "bypass": False
    }
]

print("\\n==============================================")
print(" WATER OS | ADAPTIVE CLIMATE-RESILIENT SYSTEM")
print(" PERCEIVE  ->  DECIDE  ->  ACT")
print("==============================================\\n")

step_count = 0
last_scenario = -1
scenario_duration_steps = max(1, int(18 * 1000 / timestep))

while robot.step(timestep) != -1:
    sim_time = robot.getTime()
    scenario_index = int(sim_time // 18) % len(scenarios)
    scenario = scenarios[scenario_index]

    if scenario_index != last_scenario:
        last_scenario = scenario_index
        print("\\n" + scenario["name"])
        print("PERCEIVE: pH={:.1f} | Turbidity={} NTU* | TDS={} ppm* | Salinity={}*".format(
            scenario["ph"], scenario["turbidity"], scenario["tds"], scenario["salinity"]))
        print("DECIDE: Selected route -> " + scenario["route"])
        print("ACT: Pump -> " + ("ON" if scenario["pump"] else "HOLD"))
        print("ACT: Diversion valve -> " + ("OPEN" if scenario["bypass"] else "NORMAL"))
        print("RESULT: " + ("Water held for additional treatment assessment" if scenario["bypass"]
                            else "Water transferred through modelled treatment stages"))
        print("*Illustrative simulation inputs, not real sensor measurements.")

    # Move water parcels along the visible pipe. Each particle loops around.
    for i, field in enumerate(particles):
        phase = (sim_time * 0.55 + i * 0.31) % 1.0
        x = -4.35 + phase * 8.55
        # In the hold/diversion case, show a raised branch route.
        y = 1.62 + (0.34 if scenario["bypass"] and 0.35 < phase < 0.68 else 0.0)
        z = -0.16 + (i % 6) * 0.065
        field.setSFVec3f([x, y, z])

    # Animate pump impeller while the transfer pump is enabled.
    if pump_rotation:
        angle = sim_time * (7.0 if scenario["pump"] else 0.25)
        pump_rotation.setSFRotation([0, 1, 0, angle])

    # Move the valve indicator to a visibly different position for diversion.
    if valve_translation:
        valve_translation.setSFVec3f([-0.95, 1.62 + (0.22 if scenario["bypass"] else 0.0), 0])

    step_count += 1
