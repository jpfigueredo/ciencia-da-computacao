import asyncio
import random

class Player:
    def __init__(self, name, card):
        self.name = name
        self.card = set(card)
        self.matched = set()

    def mark_number(self, number):
        if number in self.card:
            self.matched.add(number)
        return len(self.matched)

    def has_won(self):
        return self.matched == self.card

async def generator(numbers, limit=1000):
    for _ in range(limit):
        number = random.randint(0, 100)
        print(f"Number is {number}")
        await numbers.put(number)
        await asyncio.sleep(0.1)
        # Check for the winner signal
        if numbers.qsize() == 1:
            break
    await numbers.put(None)  # Signal the end

async def narrator(numbers, players):
    while True:
        number = await numbers.get()
        if number is None:
            break
        for player in players:
            count = player.mark_number(number)
            print(f"{player.name} {number} {list(player.card)} {count}")
            if player.has_won():
                print(f"{player.name} is the WINNER {player.card} {player.matched}")
                await numbers.put(None)  # Signal the generator to stop
                return

async def main():
    random.seed()
    numbers = asyncio.Queue()
    
    players_list = [
        ("player-1", [5, 10, 48, 55]),
        ("player-2", [8, 99, 80, 46]),
        ("player-3", [17, 29, 78, 95])
    ]
    
    players = [Player(name, card) for name, card in players_list]
    
    tasks = [
        asyncio.create_task(generator(numbers)),
        asyncio.create_task(narrator(numbers, players))
    ]
    
    await asyncio.gather(*tasks)
    print("Game is over")

asyncio.run(main())
