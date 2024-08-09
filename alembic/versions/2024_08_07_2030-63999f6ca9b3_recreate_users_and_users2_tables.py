"""Recreate users and users2 tables

Revision ID: 63999f6ca9b3
Revises: 08eeb50c3202
Create Date: 2024-08-07 20:30:49.645306

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63999f6ca9b3'
down_revision: Union[str, None] = '08eeb50c3202'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
