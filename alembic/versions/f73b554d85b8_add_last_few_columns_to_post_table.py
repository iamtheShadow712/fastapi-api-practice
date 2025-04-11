"""add last few columns to post table

Revision ID: f73b554d85b8
Revises: 75f78dfc939a
Create Date: 2025-04-11 06:18:39.633110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression


# revision identifiers, used by Alembic.
revision: str = 'f73b554d85b8'
down_revision: Union[str, None] = '75f78dfc939a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column('published', sa.Boolean(), server_default=expression.true(), nullable=False))
    op.add_column("posts", sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=expression.func.now()))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
