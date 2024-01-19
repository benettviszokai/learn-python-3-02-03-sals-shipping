# Sal's Shipping

# Input weight
weight = 4.8

# Flat costs
ground_flat_charge = 20
ground_premium_flat_charge = 125
drone_flat_charge = 0

# Ground Shipping fee 🚚
if weight <= 2:
  ground_cost = weight * 1.50 + ground_flat_charge
elif weight <= 6:
  ground_cost = weight * 4 + ground_flat_charge
elif weight <= 10:
  ground_cost = weight * 4 + ground_flat_charge
else:
  ground_cost = weight * 4.75 + ground_flat_charge
print("Ground Shipping fee: " + str(ground_cost) + "$")

# Ground Shipping premium fee 🚚💨
ground_premium_cost = ground_premium_flat_charge
print("Ground Shipping Premium fee: " + str(ground_premium_cost) + "$")

# Drone Shipping fee 🛸
if weight <= 2:
  drone_cost = weight * 4.50 + drone_flat_charge
elif weight <= 6:
  drone_cost = weight * 9 + drone_flat_charge
elif weight <= 10:
  drone_cost = weight * 12 + drone_flat_charge
else:
  drone_cost = weight * 14.25 + drone_flat_charge
print("Drone Shipping fee: " + str(drone_cost) + "$")

# Deciding the cheapest option
if (ground_cost <= ground_premium_cost) and (ground_cost <= drone_cost):
  print("Ground Shipping is the cheapest option: " + str(ground_cost) + "$")
elif (ground_premium_cost <= ground_cost) and (ground_premium_cost <= drone_cost):
  print("Ground Shipping Premium is the cheapest option: " + str(ground_premium_cost) + "$")
else:
  print("Drone Shipping is the cheapest option: " + str(drone_cost) + "$")
