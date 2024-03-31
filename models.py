from database import Base 
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from manager.status_manager import StatusManager

class claimstatus(Base):
    __tablename__ = 'claimstatus'

    claimid = Column(Integer, primary_key=True)
    status = Column(StatusManager)
    createdat = Column(TIMESTAMP)
    updatedat = Column(TIMESTAMP)
    digitisationstart = Column(TIMESTAMP)



if __name__ == '__main__':
    print('Models imported')