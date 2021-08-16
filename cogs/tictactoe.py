import discord
import random
from discord.ext import commands


class TTT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.player1 = None
        self.player2 = None
        self.turn = None
        self.count = 0
        self.board = []
        self.game_over = True
        self.emb = None
        self.white = ':white_large_square: '
        self.cross = ':x: '
        self.circle = ':blue_circle: '
        self.win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                    [2, 5, 8], [0, 4, 8], [2, 4, 6]]

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
        self.player1 = ctx.author
        self.player2 = p2
        players = [self.player1, self.player2]

        if self.game_over:
            self.count = 0
            desc = f'{self.player1.mention} challenges {self.player2.mention} to a tictactoe game!'

            self.emb = discord.Embed(
                title=f'{self.player1} V/S {self.player2}',
                color=discord.Color.random(),
                description=desc)

            await ctx.send(p2.mention)
            await ctx.send(embed=self.emb)

            self.board = [
                self.white, self.white, self.white, self.white, self.white,
                self.white, self.white, self.white, self.white
            ]

            #printing the board
            await self.printBoard(ctx)
            self.game_over = False

            #who starts the game

            self.turn = random.choice(players)

            await ctx.send(f"it is {self.turn.mention}'s turn!")
        else:
            await ctx.send('please finish the ongoing game first!')

    @commands.command(aliases=['p'])
    async def place(self, ctx, tile: int):
        if (ctx.author != self.turn):
            await ctx.send(
                f"it is {self.turn.mention}'s turn! please wait for your turn!"
            )
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

    @commands.command(aliases = ['r','end'])
    async def resign(self,ctx):
      if self.game_over == True:
        ctx.reply('you cant use this command right now!')
        return
      
      if ctx.author == self.player1:
        winner = self.player2
      else:
        winner = self.player1
      
      self.emb.add_field(
        name = f"{ctx.author} resigns!",
        value = f'{winner.mention} wins the game by default!'
      )
      await ctx.send(embed = self.emb)
      self.game_over = True



def setup(bot):
    bot.add_cog(TTT(bot))
    print("---> TicTacToe LOADED")