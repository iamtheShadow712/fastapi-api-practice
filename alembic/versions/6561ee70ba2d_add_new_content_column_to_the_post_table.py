"""Add new content column to the post table

Revision ID: 6561ee70ba2d
Revises: 15a1f9a038ce
Create Date: 2025-04-11 01:18:42.445503

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6561ee70ba2d'
down_revision: Union[str, None] = '15a1f9a038ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
