# main(page: Page)
# it do not work
# the hint is optional

# something in flet.app(target=main)

class Animal:
    
    def breath(self):
        print("Exhale, Inhale.")

def main(fish: Animal):
    fish.breath()
    print("Under Water.")

main()