"""Recreate users and users2 tables_ver2

Revision ID: a247504e8a0d
Revises: 63999f6ca9b3
Create Date: 2024-08-09 19:37:33.130612

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a247504e8a0d'
down_revision: Union[str, None] = '63999f6ca9b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
