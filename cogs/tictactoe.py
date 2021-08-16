import discord
import random
from discord.ext import commands


class TTT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.player1 = None
        self.player2 = None
        self.players = []
        self.draw_accepter = None
        self.turn = None
        self.count = 0
        self.board = []
        self.draw_msg = None
        self.game_over = True
        self.emb = None
        self.white = ':white_large_square: '
        self.cross = ':x: '
        self.circle = ':blue_circle: '
        self.win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                    [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        self.accept = "✅"

        self.deny = "❎"

        self.play_msg = None

    async def switch_turns(self, channel):

        if self.turn == self.player1:

            self.turn = self.player2

        elif self.turn == self.player2:

            self.turn = self.player1

        await channel.send(f"it is now {self.turn.mention}'s turn!")

    async def printBoard(self, channel):
        k = 0
        for i in range(3):
            desc = ''

            for j in range(3):

                desc += self.board[k]

                k = k + 1
            await channel.send(desc)

    @commands.command(aliases=['t'])
    async def tictactoe(self, ctx, p2: discord.Member):
        if (ctx.author == p2):
            if (ctx.author.id != 609310307218620416):
                await ctx.reply(
                    'there is no way you are so alone that you need to play tic-tac-toe with yourself. go make some friends lmao'
                )

                return

        self.player1 = ctx.author
        self.player2 = p2
        self.players = [self.player1, self.player2]

        if self.game_over:
            self.count = 0
            desc = f'{self.player1.mention} challenges {self.player2.mention} to a tictactoe game!'

            self.emb = discord.Embed(
                title=f'{self.player1} V/S {self.player2}',
                color=discord.Color.random(),
                description=desc)

            help = f'**h!t <mention player>** : challenge a player to a tic-tac-toe game \n \n**h!p <square number>** : play your move on your desired square \n \n**h!quit** : resign the game to let the other person win \n \n **h!draw** : send a draw offer to your opponent, which they can choose to accpet or decline \n\n REACT BELOW TO ACCEPT OR REJECT THE CHALLENGE'

            self.emb.add_field(name='COMMANDS', value=help)

            await ctx.send(p2.mention)
            self.play_msg = await ctx.send(embed=self.emb)

            await self.play_msg.add_reaction(self.accept)
            await self.play_msg.add_reaction(self.deny)

            self.emb.remove_field(0)

            
        else:
            await ctx.send('please finish the ongoing game first!')

    @commands.command(aliases=['p'])
    async def place(self, ctx, tile: int):
        if (ctx.author != self.turn):
            await ctx.send(
                f"it is {self.turn.mention}'s turn! please wait for your turn!"
            )
            return

        if self.game_over:
            await ctx.send('no game in progress')

            return
        #crosses go first

        if self.count % 2 == 0:
            self.board[tile - 1] = self.cross
        else:
            self.board[tile - 1] = self.circle

        await self.printBoard(ctx)

        self.count += 1

        for i in self.win:
            winCount = 0
            for j in i:
                if (self.count % 2 == 0):
                    if self.board[j] == self.cross:
                        winCount += 1
                else:
                    if self.board[j] == self.cross:
                        winCount += 1

            if winCount == 3:
                desc = f"game over! no. of rounds played = {self.count}"

                self.emb.add_field(name=f"{self.turn} won!", value=desc)
                await ctx.send(embed=self.emb)

                self.game_over = True
                return

        if (self.count == 9):

            desc = "game is a draw!"

            self.emb.add_field(name=f"DRAW!", value=desc)

            await ctx.send(embed=self.emb)
            self.game_over = True
            return

        await self.switch_turns(ctx)

    @commands.command(aliases=['r', 'end', 'quit'])
    async def resign(self, ctx):
        if self.game_over == True:
            ctx.reply('you cant use this command right now!')
            return

        if ctx.author == self.player1:
            winner = self.player2
        else:
            winner = self.player1

        self.emb.add_field(name=f"{ctx.author} resigns!",
                           value=f'{winner.mention} wins the game by default!')
        await ctx.send(embed=self.emb)
        self.game_over = True

    @commands.command()
    async def draw(self, ctx):
        if self.game_over or ctx.author not in self.players:
            await ctx.send('you are not currently in a game')
            return

        desc = f'{ctx.author.mention} is offering a DRAW! will you accept?'
        self.emb.add_field(name="DRAW OFFER", value=desc)

        if ctx.author == self.player1:
            self.draw_accepter = self.player2
            await ctx.send(self.player2.mention)
        else:
            self.draw_accepter = self.player1
            await ctx.send(self.player1.mention)

        self.draw_msg = await ctx.send(embed=self.emb)

        await self.draw_msg.add_reaction(self.accept)
        await self.draw_msg.add_reaction(self.deny)

        self.emb.remove_field(0)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        member = payload.member

        if member.bot:
            return

        if payload.message_id == self.play_msg.id:

          if member == self.player2:

            if payload.emoji.name == self.accept:

                desc = f"{self.player2} agreed to play! game on!"

                self.emb.add_field(name="ACCEPTED!", value=desc)
                await self.play_msg.channel.send(embed=self.emb)

                self.board = [
                    ':one: ', ':two: ', ':three: ', ':four: ', ':five: ',
                    ':six: ', ':seven: ', ':eight: ', ':nine: '
                ]

                #printing the board
                await self.printBoard(self.play_msg.channel)

                self.game_over = False

                #who starts the game

                self.turn = random.choice(self.players)

                await self.play_msg.channel.send(
                    f"it is {self.turn.mention}'s turn!")

            elif payload.emoji.name == self.deny:

                desc = f'{self.player2} refused to play!'

                self.emb.add_field(name="NOT ACCEPTED!", value=desc)

                await self.play_msg.channel.send(embed=self.emb)

            await self.play_msg.clear_reactions()
            self.emb.remove_field(0)

        if member != self.draw_accepter:
            return

        if payload.message_id == self.draw_msg.id:

            if payload.emoji.name == self.accept:

                desc = "both players agreed to a draw!"

                self.emb.add_field(name="DRAW!", value=desc)
                await self.draw_msg.channel.send(embed=self.emb)
                self.game_over = True

            elif payload.emoji.name == self.deny:

                desc = f'{self.draw_accepter} refused the draw! play on!'

                self.emb.add_field(name="NO DRAW!", value=desc)

                await self.draw_msg.channel.send(embed=self.emb)

            await self.draw_msg.clear_reactions()
            self.emb.remove_field(0)


def setup(bot):
    bot.add_cog(TTT(bot))
    print("---> TicTacToe LOADED")
