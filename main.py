import funciones
import argparse
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def parser():
    parser = argparse.ArgumentParser(description='Selecciona los datos que quieres ver')
    parser.add_argument('x', type=str, help='Moneda Seleccionada')
    parser.add_argument('y', type=str,help='Fecha')
    args = parser.parse_args()
    return args

def main():
    args = parser()
    x,y = args.x, args.y
    df = pd.read_csv("OUTPUT/final_table.csv")
    filter_df=info(df,x,y)
    #Historical graphic - Shows all the 'Close Prices' from 2013 to 2019
    funciones.graphic(df)
    #S. Desviation graphic - Shows the variation rate for each day.
    funciones.variation(df).plot.bar()
    plt.gcf().set_size_inches(10,10)
    plt.show()
    

def info(table,x,y):
    
    filter_table=monedaFecha(table,x,y)
    print('-------------------------------------------------------------')
    print('\n')
    print(f"Características moneda {x} a fecha {y}")
    print('\n')
    print(filter_table)
    print('\n')
    print('-------------------------------------------------------------')
    print('\n')
    print(f'CAPITALIZACION BURSATIL: Media Historica de {x} (Desde 2013 a 2019)')
    print('\n')
    print(table.groupby(['Currency']).get_group(x).mean()[3:4])
    print('\n')
    print('-------------------------------------------------------------')
    print('\n')
    print('PRECIO DE CIERRE DE TODAS MONEDAS EN MEDIAS, D.STA, GAUSS..')
    print('\n')
    print(funciones.describe(table))
    return filter_table

def monedaFecha(final_table,x,y):
    filter_table=funciones.descriptions(final_table, x, y)
    return filter_table

if __name__ == '__main__':
    main()
