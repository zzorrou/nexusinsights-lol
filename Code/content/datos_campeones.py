# datos_campeones.py
# Aquí se encuentra a modo de diccionario la información
# de los campeones con cada estadística necesaria.

# Llama a la función de la web.py en WebData/
from content.WebData.web import obtener_datos_campeones 

campeones_lista = [ 
{
    "nombre": "Ahri",
    "vida": 590,
    "daño_de_ataque": 53,
    "armadura": 21,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.668,
    "habilidades": [
        "Orb of Deception (Q)",
        "Fox-Fire (W)",
        "Charm (E)",
        "Spirit Rush (R)"
    ],
    "rol": "Mage Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 694
},
{
    "nombre": "Aatrox",
    "vida": 650,
    "daño_de_ataque": 60,
    "armadura": 38,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.651,
    "habilidades": [
        "The Darkin Blade (Q)",
        "Infernal Chains (W)",
        "Umbral Dash (E)",
        "World Ender (R)"
    ],
    "rol": "Fighter Tank",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 780
},
{
    "nombre": "Akali",
    "vida": 600,
    "daño_de_ataque": 62,
    "armadura": 23,
    "resistencia_magica": 37,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Five Point Strike (Q)",
        "Twilight Shroud (W)",
        "Shuriken Flip (E)",
        "Perfect Execution (R)"
    ],
    "rol": "Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 722
},
{
    "nombre": "Akshan",
    "vida": 630,
    "daño_de_ataque": 52,
    "armadura": 26,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.638,
    "habilidades": [
        "Avengerang (Q)",
        "Going Rogue (W)",
        "Heroic Swing (E)",
        "Comeuppance (R)"
    ],
    "rol": "Marksman Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 738
},
{
    "nombre": "Alistar",
    "vida": 685,
    "daño_de_ataque": 62,
    "armadura": 47,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Pulverize (Q)",
        "Headbutt (W)",
        "Trample (E)",
        "Unbreakable Will (R)"
    ],
    "rol": "Tank Support",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 826
},
{
    "nombre": "Ambessa",
    "vida": 630,
    "daño_de_ataque": 63,
    "armadura": 35,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Cunning Sweep (Q)",
        "Repudiation (W)",
        "Lacerate (E)",
        "Public Execution (R)"
    ],
    "rol": "Fighter Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 760
},
{
    "nombre": "Amumu",
    "vida": 685,
    "daño_de_ataque": 57,
    "armadura": 33,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.736,
    "habilidades": [
        "Bandage Toss (Q)",
        "Despair (W)",
        "Tantrum (E)",
        "Curse of the Sad Mummy (R)"
    ],
    "rol": "Tank Support",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 807
},
{
    "nombre": "Anivia",
    "vida": 550,
    "daño_de_ataque": 51,
    "armadura": 21,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Flash Frost (Q)",
        "Crystallize (W)",
        "Frostbite (E)",
        "Glacial Storm (R)"
    ],
    "rol": "Mage Support",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 652
},
{
    "nombre": "Annie",
    "vida": 560,
    "daño_de_ataque": 50,
    "armadura": 19,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.61,
    "habilidades": [
        "Disintegrate (Q)",
        "Incinerate (W)",
        "Molten Shield (E)",
        "Summon: Tibbers (R)"
    ],
    "rol": "Mage Support",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 659
},
{
    "nombre": "Aphelios",
    "vida": 600,
    "daño_de_ataque": 55,
    "armadura": 26,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.64,
    "habilidades": [
        "Weapons of the Faithful (Q)",
        "Phase (W)",
        "Weapon Queue System (E)",
        "Moonlight Vigil (R)"
    ],
    "rol": "Marksman",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 711
},
{
    "nombre": "Ashe",
    "vida": 610,
    "daño_de_ataque": 59,
    "armadura": 26,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Ranger's Focus (Q)",
        "Volley (W)",
        "Hawkshot (E)",
        "Enchanted Crystal Arrow (R)"
    ],
    "rol": "Marksman Support",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 725
},
{
    "nombre": "Aurelion Sol",
    "vida": 600,
    "daño_de_ataque": 58,
    "armadura": 22,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Breath of Light (Q)",
        "Astral Flight (W)",
        "Singularity (E)",
        "Falling Star (R)"
    ],
    "rol": "Mage",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 710
},
{
    "nombre": "Aurora",
    "vida": 607,
    "daño_de_ataque": 53,
    "armadura": 23,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.668,
    "habilidades": [
        "Twofold Hex (Q)",
        "Across the Veil (W)",
        "The Weirding (E)",
        "Between Worlds (R)"
    ],
    "rol": "Mage Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 713
},
{
    "nombre": "Azir",
    "vida": 550,
    "daño_de_ataque": 56,
    "armadura": 25,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Conquering Sands (Q)",
        "Arise! (W)",
        "Shifting Sands (E)",
        "Emperor's Divide (R)"
    ],
    "rol": "Mage Marksman",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 661
},
{
    "nombre": "Bard",
    "vida": 630,
    "daño_de_ataque": 52,
    "armadura": 34,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Cosmic Binding (Q)",
        "Caretaker's Shrine (W)",
        "Magical Journey (E)",
        "Tempered Fate (R)"
    ],
    "rol": "Support Mage",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 746
},
{
    "nombre": "Blitzcrank",
    "vida": 600,
    "daño_de_ataque": 62,
    "armadura": 37,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Rocket Grab (Q)",
        "Overdrive (W)",
        "Power Fist (E)",
        "Static Field (R)"
    ],
    "rol": "Tank Support",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 731
},
{
    "nombre": "Braum",
    "vida": 610,
    "daño_de_ataque": 55,
    "armadura": 47,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.644,
    "habilidades": [
        "Winter's Bite (Q)",
        "Stand Behind Me (W)",
        "Unbreakable (E)",
        "Glacial Fissure (R)"
    ],
    "rol": "Tank Support",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 744
},
{
    "nombre": "Briar",
    "vida": 625,
    "daño_de_ataque": 60,
    "armadura": 30,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.644,
    "habilidades": [
        "Head Rush (Q)",
        "Blood Frenzy (W)",
        "Chilling Scream (E)",
        "Certain Death (R)"
    ],
    "rol": "Fighter Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 747
},
{
    "nombre": "Caitlyn",
    "vida": 580,
    "daño_de_ataque": 60,
    "armadura": 27,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.681,
    "habilidades": [
        "Piltover Peacemaker (Q)",
        "Yordle Snap Trap (W)",
        "90 Caliber Net (E)",
        "Ace in the Hole (R)"
    ],
    "rol": "Marksman",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 697
},
{
    "nombre": "Darius",
    "vida": 652,
    "daño_de_ataque": 64,
    "armadura": 39,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Decimate (Q)",
        "Crippling Strike (W)",
        "Apprehend (E)",
        "Noxian Guillotine (R)"
    ],
    "rol": "Fighter Tank",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 787
},
{
    "nombre": "Ezreal",
    "vida": 600,
    "daño_de_ataque": 60,
    "armadura": 24,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Mystic Shot (Q)",
        "Essence Flux (W)",
        "Arcane Shift (E)",
        "Trueshot Barrage (R)"
    ],
    "rol": "Marksman Mage",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 714
},
{
    "nombre": "Fiora",
    "vida": 620,
    "daño_de_ataque": 66,
    "armadura": 33,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.69,
    "habilidades": [
        "Lunge (Q)",
        "Riposte (W)",
        "Bladework (E)",
        "Grand Challenge (R)"
    ],
    "rol": "Fighter Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 751
},
{
    "nombre": "Garen",
    "vida": 690,
    "daño_de_ataque": 69,
    "armadura": 38,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Decisive Strike (Q)",
        "Courage (W)",
        "Judgment (E)",
        "Demacian Justice (R)"
    ],
    "rol": "Fighter Tank",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 829
},
{
    "nombre": "Gragas",
    "vida": 640,
    "daño_de_ataque": 64,
    "armadura": 38,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.675,
    "habilidades": [
        "Barrel Roll (Q)",
        "Drunken Rage (W)",
        "Body Slam (E)",
        "Explosive Cask (R)"
    ],
    "rol": "Fighter Mage",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 774
},
{
    "nombre": "Heimerdinger",
    "vida": 558,
    "daño_de_ataque": 56,
    "armadura": 19,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "H-28G Evolution Turret (Q)",
        "Hextech Micro-Rockets (W)",
        "CH-2 Electron Storm Grenade (E)",
        "UPGRADE!!! (R)"
    ],
    "rol": "Mage Support",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 663
},
{
    "nombre": "Jhin",
    "vida": 655,
    "daño_de_ataque": 59,
    "armadura": 24,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Dancing Grenade (Q)",
        "Deadly Flourish (W)",
        "Captive Audience (E)",
        "Curtain Call (R)"
    ],
    "rol": "Marksman Mage",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 768
},
{
    "nombre": "Katarina",
    "vida": 672,
    "daño_de_ataque": 58,
    "armadura": 28,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Bouncing Blade (Q)",
        "Preparation (W)",
        "Shunpo (E)",
        "Death Lotus (R)"
    ],
    "rol": "Assassin Mage",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 790
},
{
    "nombre": "Lillia",
    "vida": 605,
    "daño_de_ataque": 61,
    "armadura": 22,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Blooming Blows (Q)",
        "Watch Out! Eep! (W)",
        "Swirlseed (E)",
        "Lilting Lullaby (R)"
    ],
    "rol": "Fighter Mage",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 720
},
{
    "nombre": "Lux",
    "vida": 580,
    "daño_de_ataque": 54,
    "armadura": 21,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.669,
    "habilidades": [
        "Light Binding (Q)",
        "Prismatic Barrier (W)",
        "Lucent Singularity (E)",
        "Final Spark (R)"
    ],
    "rol": "Mage Support",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 685
},
{
    "nombre": "Pantheon",
    "vida": 650,
    "daño_de_ataque": 64,
    "armadura": 40,
    "resistencia_magica": 28,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Comet Spear (Q)",
        "Shield Vault (W)",
        "Aegis Assault (E)",
        "Grand Starfall (R)"
    ],
    "rol": "Fighter Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 782
},
{
    "nombre": "Poppy",
    "vida": 610,
    "daño_de_ataque": 60,
    "armadura": 38,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Hammer Shock (Q)",
        "Steadfast Presence (W)",
        "Heroic Charge (E)",
        "Keeper's Verdict (R)"
    ],
    "rol": "Tank Fighter",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 740
},
{
    "nombre": "Rengar",
    "vida": 590,
    "daño_de_ataque": 68,
    "armadura": 34,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.667,
    "habilidades": [
        "Savagery (Q)",
        "Battle Roar (W)",
        "Bola Strike (E)",
        "Thrill of the Hunt (R)"
    ],
    "rol": "Assassin Fighter",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 724
},
{
    "nombre": "Talon",
    "vida": 658,
    "daño_de_ataque": 68,
    "armadura": 30,
    "resistencia_magica": 39,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Noxian Diplomacy (Q)",
        "Rake (W)",
        "Assassin's Path (E)",
        "Shadow Assault (R)"
    ],
    "rol": "Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 795
},
{
    "nombre": "Tristana",
    "vida": 640,
    "daño_de_ataque": 60,
    "armadura": 30,
    "resistencia_magica": 28,
    "velocidad_de_ataque": 0.656,
    "habilidades": [
        "Rapid Fire (Q)",
        "Rocket Jump (W)",
        "Explosive Charge (E)",
        "Buster Shot (R)"
    ],
    "rol": "Marksman Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 758
},
{
    "nombre": "Tryndamere",
    "vida": 696,
    "daño_de_ataque": 66,
    "armadura": 33,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.67,
    "habilidades": [
        "Bloodlust (Q)",
        "Mocking Shout (W)",
        "Spinning Slash (E)",
        "Undying Rage (R)"
    ],
    "rol": "Fighter Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 827
},
{
    "nombre": "Veigar",
    "vida": 580,
    "daño_de_ataque": 52,
    "armadura": 18,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Baleful Strike (Q)",
        "Dark Matter (W)",
        "Event Horizon (E)",
        "Primordial Burst (R)"
    ],
    "rol": "Mage",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 682
},
{
    "nombre": "Viego",
    "vida": 630,
    "daño_de_ataque": 60,
    "armadura": 34,
    "resistencia_magica": 32,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Blade of the Ruined King (Q)",
        "Spectral Maw (W)",
        "Harrowed Path (E)",
        "Heartbreaker (R)"
    ],
    "rol": "Fighter Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 756
},
{
    "nombre": "Vladimir",
    "vida": 607,
    "daño_de_ataque": 55,
    "armadura": 27,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Transfusion (Q)",
        "Sanguine Pool (W)",
        "Tides of Blood (E)",
        "Hemoplague (R)"
    ],
    "rol": "Mage Fighter",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 719
},
{
    "nombre": "Xayah",
    "vida": 630,
    "daño_de_ataque": 60,
    "armadura": 25,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Double Daggers (Q)",
        "Deadly Plumage (W)",
        "Bladecaller (E)",
        "Featherstorm (R)"
    ],
    "rol": "Marksman",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 745
},
{
    "nombre": "Xerath",
    "vida": 596,
    "daño_de_ataque": 55,
    "armadura": 22,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Arcanopulse (Q)",
        "Eye of Destruction (W)",
        "Shocking Orb (E)",
        "Rite of the Arcane (R)"
    ],
    "rol": "Mage Support",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 703
},
{
    "nombre": "Yuumi",
    "vida": 500,
    "daño_de_ataque": 49,
    "armadura": 25,
    "resistencia_magica": 25,
    "velocidad_de_ataque": 0.625,
    "habilidades": [
        "Prowling Projectile (Q)",
        "You and Me! (W)",
        "Zoomies (E)",
        "Final Chapter (R)"
    ],
    "rol": "Support Mage",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 599
},
{
    "nombre": "Zed",
    "vida": 654,
    "daño_de_ataque": 63,
    "armadura": 32,
    "resistencia_magica": 29,
    "velocidad_de_ataque": 0.651,
    "habilidades": [
        "Razor Shuriken (Q)",
        "Living Shadow (W)",
        "Shadow Slash (E)",
        "Death Mark (R)"
    ],
    "rol": "Assassin",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 778
},
{
    "nombre": "Zilean",
    "vida": 574,
    "daño_de_ataque": 52,
    "armadura": 24,
    "resistencia_magica": 30,
    "velocidad_de_ataque": 0.658,
    "habilidades": [
        "Time Bomb (Q)",
        "Rewind (W)",
        "Time Warp (E)",
        "Chronoshift (R)"
    ],
    "rol": "Support Mage",
    "porcentaje_victoria": 0,
    "porcentaje_de_baneo": 0,
    "nivel_de_poder": 680
},
]


## Función de actualización en "porcentaje_victoria" y "porcentaje_de_baneo" con
## sus respectivas winrates y banrates

def actualizar_datos_campeones():
    campeones_actuales = obtener_datos_campeones()
    for campeon in campeones_lista:
        nombre = campeon["nombre"]
        if nombre in campeones_actuales:
            campeon["porcentaje_victoria"] = float(campeones_actuales[nombre]['win_percent'].replace('%', '').strip())
            campeon["porcentaje_de_baneo"] = float(campeones_actuales[nombre]['ban_percent'].replace('%', '').strip())

# Mantén la lista de campeones disponible para la importación
if __name__ == "__main__":
    actualizar_datos_campeones()