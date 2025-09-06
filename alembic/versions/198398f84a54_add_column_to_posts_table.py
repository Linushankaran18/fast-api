"""add column to posts table

Revision ID: 198398f84a54
Revises: b270f0d56419
Create Date: 2025-09-06 11:04:25.119727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '198398f84a54'
down_revision: Union[str, Sequence[str], None] = 'b270f0d56419'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
