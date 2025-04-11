"""Add foreign key to post table

Revision ID: 75f78dfc939a
Revises: d65e9c088881
Create Date: 2025-04-11 06:12:10.709250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75f78dfc939a'
down_revision: Union[str, None] = 'd65e9c088881'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("owner_id",sa.Integer(),  nullable=False)),
    op.create_foreign_key('post_users_fk', 
                          source_table="posts",
                          referent_table="users",
                          local_cols=["owner_id"],
                          remote_cols=["id"],
                          ondelete="CASCADE"
                          )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("post_users_fk", "posts")
    op.drop_column("posts", 'owner_id')
    pass
