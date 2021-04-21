"""create_tables

Revision ID: 1c434da949b5
Revises:
Create Date: 2021-04-21 13:48:25.976872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1c434da949b5"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "Events",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user", sa.String(50)),
        sa.Column("route", sa.String(50)),
        sa.Column("address", sa.String(50)),
        sa.Column("method", sa.String(20)),
        sa.Column("request_body", sa.JSON, nullable=True),
        sa.Column("response_body", sa.JSON, nullable=True),
        sa.Column("status_code", sa.Integer),
        sa.Column("created_at", sa.DateTime(timezone=True))
    )


def downgrade():
    op.drop_table("Events")
