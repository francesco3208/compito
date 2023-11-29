from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    IDCliente = Column(String, primary_key=True)
    Nome = Column(String)
    Email = Column(String)
    Password = Column(String)

class Prodotto(Base):
    __tablename__ = 'prodotto'
    IDProdotto = Column(String, primary_key=True)
    Nome = Column(String)
    Descrizione = Column(String)
    Prezzo = Column(Integer)
    QuantitàInMagazzino = Column(Integer)

class Ordine(Base):
    __tablename__ = 'ordine'
    IDOrdine = Column(String, primary_key=True)
    DataOrdine = Column(String)
    Stato = Column(String)
    Totale = Column(Integer)
    IDCliente = Column(String, ForeignKey('cliente.IDCliente'))
    cliente = relationship("Cliente")

class DettaglioOrdine(Base):
    __tablename__ = 'dettaglio_ordine'
    IDOrdine = Column(String, ForeignKey('ordine.IDOrdine'), primary_key=True)
    IDProdotto = Column(String, ForeignKey('prodotto.IDProdotto'), primary_key=True)
    Quantità = Column(Integer)
    PrezzoUnitario = Column(Integer)
    ordine = relationship("Ordine")
    prodotto = relationship("Prodotto")

class Recensione(Base):
    __tablename__ = 'recensione'
    IDRecensione = Column(String, primary_key=True)
    Testo = Column(String)
    Voto = Column(Integer)
    Data = Column(String)
    IDCliente = Column(String, ForeignKey('cliente.IDCliente'))
    IDProdotto = Column(String, ForeignKey('prodotto.IDProdotto'))
    cliente = relationship("Cliente")
    prodotto = relationship("Prodotto")

class Fornitore(Base):
    __tablename__ = 'fornitore'
    IDFornitore = Column(String, primary_key=True)
    Nome = Column(String)
    Contatto = Column(String)

engine = create_engine('sqlite:///ecommerce.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def aggiungi_cliente(id_cliente, nome, email, password):
    nuovo_cliente = Cliente(IDCliente=id_cliente, Nome=nome, Email=email, Password=password)
    session.add(nuovo_cliente)
    session.commit()

def leggi_clienti():
    return session.query(Cliente).all()

if __name__ == "__main__":
    aggiungi_cliente('C001', 'Francesco Spedicato', 'francesco@mail.com', 'password')
    clienti = leggi_clienti()
    for cliente in clienti:
        print(cliente.Nome, cliente.Email)
