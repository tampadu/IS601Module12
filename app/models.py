from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    result = Column(Float, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    user = relationship("User", back_populates="calculations")

    def compute_result(self):
        if self.type == "Add":
            return self.a + self.b
        elif self.type == "Sub":
            return self.a - self.b
        elif self.type == "Multiply":
            return self.a * self.b
        elif self.type == "Divide":
            if self.b == 0:
                raise ValueError("Cannot divide by zero")
            return self.a / self.b
        else:
            raise ValueError(f"Unknown calculation type {self.type}")
