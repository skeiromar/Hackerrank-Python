if __name__ == '__main__':
    Names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Names.extend([[name, score]])
    minOf = [[x, o] for x, o in Names if o > min([o for p, o in Names])]
    print('\n'.join(sorted([i for i, l in minOf if l == min([o for p, o in minOf])])))
