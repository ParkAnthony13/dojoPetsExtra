from ninja import Ninja
from pet import Pet
from pet import Demon



bubbles = Pet("Bubbles", "dog", "Roll over", "Bark")
meNinja = Ninja("Ant","Park","ham","kibble",bubbles)

meNinja.bathe().feed().walk().check_status()

bubbles2 = Demon("Bubbles2", "demon hound", "Kill")

handler = Ninja("Hunter","O'dimones","ham","kibble",bubbles2)

handler.walk().check_status()