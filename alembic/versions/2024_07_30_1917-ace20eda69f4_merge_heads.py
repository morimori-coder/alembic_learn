"""merge heads

Revision ID: ace20eda69f4
Revises: f2932c930d16, 4d7892bafc34
Create Date: 2024-07-30 19:17:49.469681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ace20eda69f4'
down_revision: Union[str, None] = ('f2932c930d16', '4d7892bafc34')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
