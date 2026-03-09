class ModelBasedReflexAgent:
    def __init__(self):
        self.previous_action = "OFF"   # Heater initially OFF

    def decide(self, temperature):
        print(f"\nCurrent Temperature: {temperature}°C")
        print(f"Previous Heater State: {self.previous_action}")

        # Decision rules
        if temperature < 20:
            if self.previous_action != "ON":
                self.previous_action = "ON"
                print("Action: Turning Heater ON")
            else:
                print("Action: Heater already ON (No change)")

        elif temperature > 25:
            if self.previous_action != "OFF":
                self.previous_action = "OFF"
                print("Action: Turning Heater OFF")
            else:
                print("Action: Heater already OFF (No change)")

        else:
            print("Action: Temperature normal, keeping previous state")

        return self.previous_action


# ---- Testing the Agent ----
agent = ModelBasedReflexAgent()

# Simulated temperature readings
temperatures = [18, 19, 22, 27, 26, 23, 17]

for temp in temperatures:
    agent.decide(temp)