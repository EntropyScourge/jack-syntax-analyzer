import sys
import JackTokenizer as jt

a = jt.JackTokenizer(open(sys.argv[1]).read())
#a = jt.JackTokenizer('class fuckwit{}\n// This file is part of www.nand2tetris.org\n.')#// and the book "The Elements of Computing Systems"\n// by Nisan and Schocken, MIT Press.\n/// File name: projects/10/ExpressionLessSquare/Square.jack\n\n/** Expressionless version of projects/10/Square/Square.jack. */\n\nclass Square {\n\n   field int x, y; \n   field int size; \n\n   constructor Square new(int Ax, int Ay, int Asize) {\n      let x = Ax;\n      let y = Ay;\n      let size = Asize;\n      do draw();\n      return x;\n   }\n\n   method void dispose() {\n      do Memory.deAlloc(this);\n      return;\n   }\n\n   method void draw() {\n      do Screen.setColor(x);\n      do Screen.drawRectangle(x, y, x, y);\n      return;\n   }\n\n   method void erase() {\n      do Screen.setColor(x);\n      do Screen.drawRectangle(x, y, x, y);\n      return;\n   }\n\n   method void incSize() {\n      if (x) {\n         do erase();\n         let size = size;\n         do draw();\n      }\n      return;\n   }\n\n   method void decSize() {\n      if (size) {\n         do erase();\n         let size = size;\n         do draw();\n      }\n      return;\n   }\n\n   method void moveUp() {\n      if (y) {\n         do Screen.setColor(x);\n         do Screen.drawRectangle(x, y, x, y);\n         let y = y;\n         do Screen.setColor(x);\n         do Screen.drawRectangle(x, y, x, y);\n      }\n      return;\n   }\n\n   method void moveDown() {\n      if (y) {\n         do Screen.setColor(x);\n         do Screen.drawRectangle(x, y, x, y);\n         let y = y;\n         do Screen.setColor(x);\n         do Screen.drawRectangle(x, y, x, y);\n      }\n      return;\n   }\n\n   method void moveLeft() {\n      if (x) {\n         do Screen.setColor(x);\n         do Screen.drawRectangle(x, y, x, y);\n         let x = x;\n         do Screen.setColor(x);\n         do Screen.drawRectangle(x, y, x, y);\n      }\n      return;\n   }\n\n   method void moveRight() {\n      if (x) {\n         do Screen.setColor(x);\n         do Screen.drawRectangle(x, y, x, y);\n         let x = x;\n         do Screen.setColor(x);\n         do Screen.drawRectangle(x, y, x, y);\n      }\n      return;\n   }\n}  \n')
#print([open(sys.argv[1]).read()])

while a.hasMoreTokens():
    a.advance()
print(a.tokenList)