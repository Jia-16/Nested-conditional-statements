print("Step uno: Pick a vehicle!!")
print("1 - Car!")
print("2 - Motorcycle :)")
print("\n")

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    print("You are automatically my favourite (don't tell the people who chose cars I told you that). Now, pick your bike type.")
    print("1 - Honda. (quite standard, but great quality)")
    print("2 - Yamaha. (everyone nows that brand of bike, and this brand makes EVERYTHING)")
    bikeType = int(input("Enter 1 or 2: "))

    if bikeType == 1:
        print("Okayyy, I see youu. YOU PICKED THE HONDAAA!!!!")
        print("SPEED: 150KM/H")
        print("Best feature: It's AMAZING. It can handle tough terrain adn great for the people who love driving off road. And you will look sick, I mean, yeah GET IT QUEEN/KING.")

    else:
        print("Basic but okay. Yamaha's a good brand and the most favourable brand, considering their random products")
        print("SPEED: 155 KM/H")
        print("Best Features: This brand is optimal to look cool as hell. it's great for driving around the streets and for whatever tricks to wanna try or use it for a tiktok trend, I don't care, just enjoy life with the Yamaha, you've earnt it.")

elif choice == 2:
    print("Step uno + uno: Pick your car type")
    print("1 - Sedan: it's practical as it isn't a tank but not some clown car, easy ot maintain and has...reasonable...car space.")
    print("2 - SUV: great if you have a family of 5 and a dog that tends to take up most of the seats, but you are too hearted to kick it out Peanut Butter or something cause quote unquote: HE'S JUST A BABYYY!!; but it's okay I feel that too and I don't even have a dog.")
    carType = int(input("Enter 1 or 2: "))
    if carType == 1:
        print("Ahh, you chose the Sedan because you have a very small family or you just don't have that much stuff to carry around. Respect.")
        print("SPEED: 200 KM\H")
        print("Best Feature: Easier to steer and petrol tank has less capacity, saving you money, these prices are CRAZYYYY. I mean, 223.9 dolars for FUEL. AWH HECK NAWWWW! What is happening in this economy, next thing we know, it's going to be $100,000 or something like that.")
    else:
        print("Okay, I get it. This one is the best choice if you want space and room to fit seven people in it. great for going out with the mates for a hangout and the local arcade and have a great summer time. I'm jealous. *jumps into car* I CALL SHOTGUN! AND NO I DON'T CARE IF IT'S ALREADY BE CALLED.")
else:
    print("That is not a valid choice. ")
    print("Please enter 1 for bike and 2 for car.")

print()
print("==================================================")
print("YOU RIDE IS READY FOR YOU TO ENJOY!!!")
print("Please do not crash, I know you want to take it for a spin, but be careful, I don't want you hurt.")
print("==================================================")