# Let's test routing line from Super Admin to Melihat Dashboard on Left Side Stack
# If all 3 actors are on the left:
# Super Admin: cx=160, cy=220 (hand: 200, 215)
# Site Supervisor: cx=160, cy=490 (hand: 200, 485)
# Branch Manager: cx=160, cy=760 (hand: 200, 755)

# If Row order in Column 1:
# What if Row 1: Melihat Dashboard & Klasemen?
# Then Super Admin (215) connects to Row 1 (190)
# Site Supervisor (485) connects to Row 1 (190)
# Branch Manager (755) connects to Row 1 (190)
# But Supervisor to Row 1 crosses Admin to Row 2!

# What if:
# In UML, when all actors share a use case:
# We can route Super Admin line around, OR
# What if Actor Generalization?
# User (Pengguna) is parent actor of Super Admin, Supervisor, Manager.
# Or what if direct line with a dogleg / orthogonal routing?
# Or what if Two-Sided: ISS on left, Prodia on right?
